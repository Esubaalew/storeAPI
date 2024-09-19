from rest_framework import viewsets
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


# Brand ViewSet
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


# Model ViewSet
class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


# Item ViewSet
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# Stock ViewSet
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


# Stock Availability View (Retrieve)
class StockAvailabilityView(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockAvailabilitySerializer
    lookup_field = 'item_id'
