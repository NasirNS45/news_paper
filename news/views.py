from django.shortcuts import render
from django.views.generic import View
from . import models


class HomeView(View):

    def get(self, request):
        categories = models.Category.objects.all()
        return render(request, "index.html", {"categories": categories})


class NewsView(View):

    def get(self, request):
        news = models.News.objects.all()
        return render(request, "news.html", {"news": news})


class CategoryView(View):
    def get(self, request, slug):
        news = models.News.objects.filter(category__slug__icontains=slug)
        return render(request, "category.html", {"news": news})
