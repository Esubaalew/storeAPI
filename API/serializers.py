from rest_framework import serializers
from .models import Category, Subcategory, Brand, Model, Item, Stock


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    subcategory = serializers.CharField(source='subcategory.name', read_only=True)
    brand = serializers.CharField(source='brand.name', read_only=True)
    model = serializers.CharField(source='model.name', read_only=True)

    class Meta:
        model = Item
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    class Meta:
        model = Stock
        fields = '__all__'


class StockAvailabilitySerializer(serializers.ModelSerializer):
    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = ['item', 'quantity', 'is_available']

    def get_is_available(self, obj):
        return obj.is_available()
