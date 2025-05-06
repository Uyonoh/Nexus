from django.urls import path, include
from . import views

app_name = "products"
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<str:name>/', views.product_detail, name='product_detail'),
    path('categories/<str:category>/', views.category_list, name='category_products'),
]