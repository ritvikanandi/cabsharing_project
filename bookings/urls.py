from django.urls import path, include
from . import views

urlpatterns = [
    path('createbooking/', views.createbooking, name='createbooking'),
]
