
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('partial/', views.cart_partial, name='cart_partial'),
    path('items-partial/', views.cart_items_partial, name='items_partial'),
    path("nav-cart-partial", views.nav_cart_partial, name="nav_cart_partial"),
]