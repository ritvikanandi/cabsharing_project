from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name = 'bookings'),
    path('feedback/', views.feedback_view, name='feedback'),
]
