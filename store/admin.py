from django.contrib import admin
from .models import Category, ProductType, Product, Order, OrderItem, Inventory, Review

admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Inventory)
admin.site.register(Review)
