from django.contrib import admin
from .models import Category, Subcategory, Brand, Model, Item, Stock

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Item)
admin.site.register(Stock)
