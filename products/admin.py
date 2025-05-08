from django.contrib import admin
from .models import Category, Product, ProductImage, ProductSpec, ProductType
#  Order, OrderItem, ShippingAddress, Review, Contact, OrderStatus, PaymentStatus, Payment, Coupon, CouponUsage,

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductSpec)
admin.site.register(ProductType)