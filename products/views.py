from django.http import HttpRequest
from django.shortcuts import render, redirect

from django_htmx.http import trigger_client_event
from rest_framework import generics
from django.shortcuts import render
from .models import Category, ProductType, Product, ProductImage, ProductSpec
from .serializers import CategorySerializer, ProductTypeSerializer, ProductSerializer

from typing import List, Dict, Tuple
import random
from .forms import ProductForm, ProductImageForm, ProductSpecForm

CategoriesProducts = Dict[str, List[Product]]
# HttpRequest.

def product_list(request):
    # products = Product.objects.all()
    products = get_products()
    return render(request, 'frontend/product_list2.html', {'products': products})

def product_detail(request, name: str):
    product = Product.objects.get(name=name)
    product = ProductSerializer(product).data
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

def add(request):
    product: Product = None
    if request.method == "POST":
        if request.POST.get("form") == "product":
            form = ProductForm(request.POST, request.FILES)

            if form.is_valid():
                product = form.save()
                # trigger_client_event(request, 'addImages')
                form = ProductSpecForm()
                return render(request, 'products/includes/add_spec.html', {"form": form, "product_id": product.id})
            else:
                return render(request, 'products/add.html', {"form": form})
            
        elif request.POST.get("form") == "spec":
            form = ProductSpecForm(request.POST)
            id = request.POST.get("product_id")
            product = Product.objects.get(id=id)
            form.instance.product = product

            print(form)
            if form.is_valid():
                product_spec: ProductSpec = form.save()
                # trigger_client_event(request, 'finishProduct')
                
                form = ProductImageForm()
                return render(request, 'products/includes/add_images.html', {"form": form, "product_id": product.id})
            else:
                return render(request, 'products/includes/add_spec.html', {"form": form, "product_id": product.id})

        else:
            form = ProductImageForm(request.POST, request.FILES)
            id = request.POST.get("product_id")
            product = Product.objects.get(id=id)
            form.instance.product = product
            # print(request.body)
            if form.is_valid():
                product_image: ProductImage = form.save()
                # trigger_client_event(request, 'addSpec')
                return redirect('frontend:home')
            else:
                print(form.errors)
                return render(request, 'products/includes/add_images.html', {"form": form, "product_id": product.id})
            
        
            
    else:
        form = ProductForm()

    
    return render(request, 'products/add.html', {"form": form})