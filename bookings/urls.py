from django.urls import path
from . import views

urlpatterns = [
    path('', views.filter_bookings, name = 'bookings'),
    path('create/', views.create_booking, name = 'createbooking'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('<int:booking_id>/join', views.join_booking, name='join'),
    path('<int:booking_id>/leave', views.leave_booking, name='leave'),
    path('<int:booking_id>/info', views.booking_info, name='booking_info'),
    path('filter/', views.filter_bookings, name = 'filter'),
]
