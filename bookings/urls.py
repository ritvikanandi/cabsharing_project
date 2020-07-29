from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'bookings'),
    path('create/', views.create_booking, name = 'createbooking'),
    path('feedback/', views.feedback_view, name='feedback'),
]