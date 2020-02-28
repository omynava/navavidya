from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Course


class HomeView(ListView):
    model = Course
    paginate_by = 10
    template_name = "base.html"
