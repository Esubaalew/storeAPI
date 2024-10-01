from django.contrib import admin
from .models import Category, Subcategory, Brand, Model, Item, Stock, Request, Message


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 10


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category__name')
    ordering = ('category', 'name')
    list_per_page = 10


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory')
    search_fields = ('name', 'subcategory__name')
    ordering = ('subcategory', 'name')
    list_per_page = 10


class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'subcategory')
    search_fields = ('name', 'brand__name', 'subcategory__name')
    ordering = ('brand', 'subcategory', 'name')
    list_per_page = 10


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Stock)
admin.site.register(Request)

# changing the titles
admin.site.site_title = 'Milka'
admin.site.site_header = 'Milka'
