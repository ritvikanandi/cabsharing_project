from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'bookings'),
    path('create/', views.create_booking, name = 'createbooking'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('update/', views.update_booking, name='update'),
    path('<int:booking_id>', views.detail, name='detail'),
    path('<int:booking_id>/join', views.join, name='join'),
    path('<int:booking_id>/leave', views.leave, name='leave'),
]
