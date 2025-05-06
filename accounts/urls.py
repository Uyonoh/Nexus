from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from . import views
from frontend.views import landing2

app_name = "accounts"

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='frontend:home'), name='logout'),
    path("profile/", views.user_profile, name="profile"),
    path("", landing2, name="orders"),
]

