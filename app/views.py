from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Course, Category


class HomeView(ListView):
    model = Course
    template_name = "home.html"


class HomeCategoryView(ListView):
    model = Category
    template_name = "home.html"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "course-grid.html"
