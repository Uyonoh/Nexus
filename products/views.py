from django.shortcuts import render

from rest_framework import generics
from django.shortcuts import render
from .models import Category, ProductType, Product
from .serializers import CategorySerializer, ProductTypeSerializer, ProductSerializer

from typing import List, Dict, Tuple
import random

CategoriesProducts = Dict[str, List[Product]]


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