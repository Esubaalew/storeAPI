from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, SubcategoryViewSet, BrandViewSet, ModelViewSet,
    ItemViewSet, StockViewSet, StockAvailabilityView
)


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'models', ModelViewSet)
router.register(r'items', ItemViewSet)
router.register(r'stocks', StockViewSet)


urlpatterns = [
    path('items/<int:item_id>/stocks/', StockAvailabilityView.as_view({'get': 'retrieve'}), name='stock-availability'),
    path('', include(router.urls)),
]
