from django import forms
from django.contrib.auth.models import User
from .models import Feedback
from .models import createbooking
import datetime

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['details']


class BookingForm(forms.ModelForm):
    time = forms.TimeField(widget=forms.TimeInput, label="Time (Enter in format hh:mm:ss)")
    date = forms.DateField(widget=forms.DateInput ,initial=datetime.date.today)
    pickup = forms.CharField(label = "Pick Up Location")
    destination = forms.CharField(label = "Drop Location")
    peopletogether = forms.IntegerField(label = "People Together")
    luggage = forms.DecimalField(widget = forms.NumberInput, label = "Amount of luggage",)
    budget = forms.CharField(label = "Your budget")

    class Meta:
        model = createbooking
<<<<<<< HEAD
        fields = ['time', 'date', 'pickup', 'destination', 'luggage', 'budget']
=======
        fields = ['time', 'date', 'pickup', 'destination' ,'peopletogether', 'luggage', 'budget']
>>>>>>> 9707b91aa08f71c60f8b3f3b605d7bd060254610
