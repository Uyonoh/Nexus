from django.urls import path, include
from . import views

app_name = "products"
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('detail/<str:name>/', views.product_detail, name='product_detail'),
    path('categories/<str:category>/', views.category_list, name='category_products'),
    path('add/', views.add, name="add"),
    path('add-image-field/', views.add_image_field, name='add_image_field'),
    path('add-spec-field/', views.add_spec_field, name='add_spec_field'),
    path('remove-field/', views.remove_field, name='remove_field'),
]