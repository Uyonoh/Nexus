from django.urls import path, include
from products import views

app_name = "frontend"

urlpatterns = [
    path("", views.landing2, name="home"),
    path("landing", views.landing2, name="landing2"),
]