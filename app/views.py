from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Course, Category, CourseDetail


class HomeView(ListView):
    model = Category
    template_name = "home.html"


class CourseView(ListView):
    model = Course
    template_name = "course-grid.html"


class CourseDetailView(ListView):
    model = CourseDetail
    template_name = "course-details.html"
