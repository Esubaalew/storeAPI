from django.db import models


# Category model
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Subcategory model
class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


# Brand model
class Brand(models.Model):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(Subcategory, related_name='brands', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.subcategory.name} - {self.name}"


# Model under a brand
class Model(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, related_name='models', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='models', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.brand.name} - {self.name}"


# Item model
class Item(models.Model):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(Subcategory, related_name='items', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='items', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Stock model
class Stock(models.Model):
    item = models.OneToOneField(Item, related_name='stock', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def is_available(self):
        return self.quantity > 0

    def __str__(self):
        return f"{self.item.name} - {self.quantity} pcs"


class Request(models.Model):
    user_id = models.CharField(max_length=255) 
    username = models.CharField(max_length=255, blank=True, null=True)  
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50) 
    address = models.TextField() 
    additional_text = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True) 
    is_responded = models.BooleanField(default=False) 

    def __str__(self):
        return f"Request from {self.name} (User ID: {self.user_id})"


class Message(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    sender_id = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender_id} on {self.created_at}"