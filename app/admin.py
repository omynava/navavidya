from django.contrib import admin
from .models import Course, Category, CourseDetail

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(CourseDetail)

