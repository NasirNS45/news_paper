from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("news", views.NewsView.as_view(), name="news"),
    path("category/<str:slug>", views.CategoryView.as_view(), name="category")
]
