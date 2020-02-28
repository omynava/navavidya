from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Course


class HomeView(ListView):
    model = Course
    template_name = "base.html"
