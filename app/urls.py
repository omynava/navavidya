from django.urls import path
from .views import HomeView, CategoryDetailView

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>/', CategoryDetailView.as_view(), name='course-grid.html')

]



