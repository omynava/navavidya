from django.urls import path
from .views import HomeView, CourseView, CourseDetailView

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('course/<slug>/', CourseView.as_view(), name='course'),
    path('course-detail/<slug>/', CourseDetailView.as_view(), name='course-detail')

]

