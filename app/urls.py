from django.urls import path
from .views import HomeView, CourseView, CourseDetailView, add_to_cart

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('course/<slug>/', CourseView.as_view(), name='course'),
    path('course-detail/<slug>/', CourseDetailView.as_view(), name='course-detail'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart')

]

