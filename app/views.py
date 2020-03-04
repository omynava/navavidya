from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Course, Category, Order, OrderCourse
from django.contrib import messages
from django.utils import timezone


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
        if order.courses.filter(course__slug=course.slug).exists():
            order_course.quantity += 1
            order_course.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            order.items.add(order_course)
            messages.info(request, "This item was added to your cart.")
            return redirect("core:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.course.add(order_course)
        messages.info(request, "This item was added to your cart.")
        return redirect("core:order-summary")


def remove_from_cart(request, slug):
    course = get_object_or_404(Course, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.cousre.filter(course__slug=course.slug).exists():
            order_course = OrderCourse.objects.filter(
                course=course,
                user=request.user,
                ordered=False
            )[0]
            order.course.remove(order_course)
            order_course.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)


def remove_single_course_from_cart(request, slug):
    course = get_object_or_404(Course, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.course.filter(item__slug=course.slug).exists():
            order_course = OrderCourse.objects.filter(
                course=course,
                user=request.user,
                ordered=False
            )[0]
            if order_course.quantity > 1:
                order_course.quantity -= 1
                order_course.save()
            else:
                order.course.remove(order_course)
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)
