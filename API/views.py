from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Subcategory, Brand, Model, Item, Stock
from .serializers import (
    CategorySerializer, SubcategorySerializer, BrandSerializer, ModelSerializer,
    ItemSerializer, StockSerializer, StockAvailabilitySerializer
)

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Subcategory ViewSet
class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

    # Custom action to get subcategories by category
    @action(detail=False, methods=['get'])
    def by_category(self, request, category_pk=None):
        category_id = request.query_params.get('category')
        if category_id:
            subcategories = self.queryset.filter(category__id=category_id)
            serializer = self.get_serializer(subcategories, many=True)
            return Response(serializer.data)
        return Response([])


# Brand ViewSet
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    # Custom action to get brands by subcategory
    @action(detail=False, methods=['get'])
    def by_subcategory(self, request, subcategory_pk=None):
        subcategory_id = request.query_params.get('subcategory')
        if subcategory_id:
            brands = self.queryset.filter(subcategory__id=subcategory_id)
            serializer = self.get_serializer(brands, many=True)
            return Response(serializer.data)
        return Response([])


# Model ViewSet
class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

    # Custom action to get models by brand
    @action(detail=False, methods=['get'])
    def by_brand(self, request, brand_pk=None):
        brand_id = request.query_params.get('brand')
        if brand_id:
            models = self.queryset.filter(brand__id=brand_id)
            serializer = self.get_serializer(models, many=True)
            return Response(serializer.data)
        return Response([])


# Item ViewSet
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # Custom action to get items by model
    @action(detail=False, methods=['get'])
    def by_model(self, request, model_pk=None):
        model_id = request.query_params.get('model')
        if model_id:
            items = self.queryset.filter(model__id=model_id)
            serializer = self.get_serializer(items, many=True)
            return Response(serializer.data)
        return Response([])


# Stock ViewSet
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


# Stock Availability View (Retrieve)
class StockAvailabilityView(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockAvailabilitySerializer
    lookup_field = 'item_id'
