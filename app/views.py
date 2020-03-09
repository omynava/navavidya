from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from .models import Course, Category, Order, OrderCourse
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import login, authenticate

class HomeView(ListView):
    model = Category
    template_name = "home.html"


class CourseView(ListView):
    model = Course
    template_name = "course-grid.html"


class CourseDetailView(DetailView):
    model = Course
    template_name = "course-details.html"


def add_to_cart(request, slug):
    course = get_object_or_404(Course, slug=slug)
    order_course, created = OrderCourse.objects.get_or_create(
        course=course,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.course.filter(course__slug=course.slug).exists():
            order_course.quantity += 1
            order_course.save()
            messages.info(request, "This Course quantity was updated.")
            return redirect("app:course-detail", slug=slug)
        else:
            order.course.add(order_course)
            messages.info(request, "This item was added to your cart.")
            return redirect("app:course-detail", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.course.add(order_course)
        messages.info(request, "This item was added to your cart.")
        return redirect("app:course-detail", slug=slug)




