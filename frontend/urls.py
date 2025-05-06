from django.urls import path, include
from . import views

app_name = "frontend"

urlpatterns = [
    path("", views.landing2, name="home"),
    path("landing", views.landing2, name="landing2"),
    # path('products/', views.product_list, name='product_list'),
    # path('products/<str:name>/', views.product_detail, name='product_detail'),
    # path('categories/<str:category>/', views.category_list, name='category_products'),
    # path('user/', views.get_user, name='user_account'),
]