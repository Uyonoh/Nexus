from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('product_type/', views.ProductTypeList.as_view(), name='product-type-list'),
    path('product_type/<int:pk>/', views.ProductTypeDetail.as_view(), name='product-type-detail'),
    path('products/', views.ProductList.as_view(), name='product-list-api'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail-api'),
    path('orders/', views.OrderList.as_view(), name='order-list-api'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order-detail-api'),
    path('orderitems/', views.OrderItemList.as_view(), name='orderitem-list-api'),
    path('orderitems/<int:pk>/', views.OrderItemDetail.as_view(), name='orderitem-detail-api'),
    path('inventory/', views.InventoryList.as_view(), name='inventory-list-api'),
    path('inventory/<int:pk>/', views.InventoryDetail.as_view(), name='inventory-detail-api'),
    # path('products_template/', views.product_list, name='product_list'),
    # path('products_template/<int:pk>/', views.product_detail, name='product_detail'),
    # path('categories_template/<str:category>/', views.category_list, name='category_products'),
    # path('', views.landing, name='landing'),
]
