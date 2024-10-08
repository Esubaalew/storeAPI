from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Subcategory, Brand, Model, Item, Stock, Request, Message
from .serializers import (
    CategorySerializer, SubcategorySerializer, BrandSerializer, ModelSerializer,
    ItemSerializer, StockSerializer, StockAvailabilitySerializer, 
    RequestSerializer,
      MessageSerializer
)


# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def subcategories(self, request, pk=None):
        category = self.get_object()
        subcategories = category.subcategories.all()
        serializer = SubcategorySerializer(subcategories, many=True)
        return Response(serializer.data)


# Subcategory ViewSet
class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        subcategory = self.get_object()
        items = subcategory.items.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def brands(self, request, pk=None):
        subcategory = self.get_object()
        brands = subcategory.brands.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)


# Brand ViewSet
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @action(detail=True, methods=['get'])
    def models(self, request, pk=None):
        brand = self.get_object()
        models = brand.models.all()
        serializer = ModelSerializer(models, many=True)
        return Response(serializer.data)


# Model ViewSet
class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        model = self.get_object()
        items = model.items.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


# Item ViewSet
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=True, methods=['get'])
    def stocks(self, request, pk=None):
        item = self.get_object()
        stocks = item.stocks.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', None)
        if query:
            items = Item.objects.filter(name__icontains=query)  # Case-insensitive search
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data)
        return Response({"error": "No search query provided."}, status=400)


# Stock ViewSet
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    @action(detail=True, methods=['get'])
    def item(self, request, pk=None):
        stock = self.get_object()
        item = stock.item
        serializer = ItemSerializer(item)
        return Response(serializer.data)


# Stock Availability View (Retrieve)
class StockAvailabilityView(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockAvailabilitySerializer
    lookup_field = 'item_id'

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def update(self, request, pk):
        # Mark the request as responded
        request_instance = self.get_object()
        request_instance.is_responded = True
        request_instance.save()

        return Response({"status": "Request marked as responded."})

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request):
        # Deserialize and validate the incoming data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract the validated data
        validated_data = serializer.validated_data
        request_instance = validated_data.get('request')
        sender_id = validated_data.get('sender_id')

        
        if request_instance.user_id == sender_id:
            
            request_instance.is_responded = True
            request_instance.save()

       
        serializer.save()

        return Response(serializer.data)
