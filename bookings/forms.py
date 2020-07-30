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
    max = forms.IntegerField(label = "Maximum members")

    class Meta:
        model = createbooking
        fields = ['time', 'date', 'pickup', 'destination' ,'peopletogether', 'luggage', 'budget','max']
