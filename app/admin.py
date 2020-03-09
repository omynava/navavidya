from django.contrib import admin
from .models import Course, Category, OrderCourse, Order

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(OrderCourse)
admin.site.register(Order)

