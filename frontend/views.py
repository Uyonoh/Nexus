from django.shortcuts import render

from rest_framework import generics
from django.shortcuts import render
from products.models import Category, ProductType, Product#, Order, OrderItem, Inventory
from products.serializers import CategorySerializer, ProductTypeSerializer, ProductSerializer #, OrderSerializer, OrderItemSerializer, InventorySerializer

from .products import products, reviews, related_products
from typing import List, Dict, Tuple
import random

CategoriesProducts = Dict[str, List[Product]]

detail_product = {
    "id": 1,
    "name": "ProBook X7 Ultra",
    "description": '15.6" Gaming Laptop, RTX 4080, 32GB RAM, 2TB SSD',
    "price": 2499.99,
    "rating": 5,
    "reviewCount": 128,
    "stock": 15,
    "images": [
        'https://images.unsplash.com/photo-1603302576837-37561b2e2302?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
        'https://images.unsplash.com/photo-1602080858428-57174f9431cf?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
        'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80',
        'https://images.unsplash.com/photo-1593642632823-8f785ba67e45?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80'
    ],
    "specs": {
        "processor": "Intel Core i9-13900H",
        "graphics": "NVIDIA GeForce RTX 4080 16GB",
        "memory": "32GB DDR5-5200MHz",
        "storage": "2TB NVMe PCIe Gen4 SSD",
        "display": '15.6" QHD+ 240Hz',
        "os": "Windows 11 Pro",
        "battery": "99.9WHr",
        "weight": "2.3kg"
    },
    "reviews": reviews,
    "related_products": related_products,
}


def product_list(request):
    # products = Product.objects.all()
    products = get_products()
    return render(request, 'frontend/product_list2.html', {'products': products})

def product_detail(request, name: str):
    product = Product.objects.get(name=name)
    return render(request, 'frontend/product_detail2.html', {'product': product})

def category_list(request, category: str):
    products = get_products_by_category(category)
    # products = products[list(products.keys())[random.randint(0, len(products.keys()) - 1)]]
    return render(request, 'frontend/category2.html', {'products': products})

def landing(request):
    return render(request, 'frontend/landing.html')


def add_products():
    # print(type(products))
    for cat, prods in products.items():
        for prod in prods:
            prod["product_type"] = random.randint(1, 3)
            prod["category"] = random.randint(1, 3)
            product = ProductSerializer(data=prod)
            if product.is_valid():
                product.save()
            else:
                print(product.errors)

def get_products() -> Dict[str, List[Product]]:
    products = {}
    queryset = Product.objects.all()
    products["Products"] = [ProductSerializer(product).data for product in queryset]

    return products

def get_products_by_category(category) -> List[Product]:

    category_id = Category.objects.get(name=category).id
    queryset = Product.objects.filter(category=category_id)
    return [ ProductSerializer(product).data for product in queryset]

def get_categories() -> Dict[str, List[Product]]:
    products = {}
    categories = Category.objects.all()
    for category in categories:
        products[f"{category}"] = get_products_by_category(category)
    return products
    

def landing2(request):
    # Fetch products by category
    # organize into dicts in products list
    
    products = get_categories()
    return render(request, 'frontend/landing2.html', {"products": products})

def get_user(request):
    return render(request, 'frontend/landing.html')
