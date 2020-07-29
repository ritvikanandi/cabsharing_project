from django import forms
from django.contrib.auth.models import User
from .models import createbooking
import datetime

class BookingForm(forms.ModelForm):
    time = forms.TimeField(widget=forms.TimeInput, label="Time (Enter in format hh:mm:ss)")
    date = forms.DateField(widget=forms.DateInput ,initial=datetime.date.today)
    pickup = forms.CharField(label = "Pick Up Location")
    destination = forms.CharField(label = "Drop Location")
    luggage = forms.DecimalField(widget = forms.NumberInput, label = "Amount of luggage",)
    budget = forms.CharField(label = "Your budget")

    class Meta:
        model = User
        fields = ['time', 'date', 'pickup', 'destination', 'luggage', 'budget']
