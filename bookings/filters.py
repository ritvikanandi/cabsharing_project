from django.contrib.auth.models import User
import django_filters
from .models import createbooking, Member



class BookingFilter(django_filters.FilterSet):
    destination = django_filters.CharFilter(lookup_expr='iexact')
    pickup = django_filters.CharFilter(lookup_expr='iexact')
    date = django_filters.DateFilter(lookup_expr='iexact')
    time = django_filters.TimeFilter(lookup_expr='lt')

    class Meta:
        model = createbooking
        fields = ['destination', 'pickup', 'date' , 'time' ]
