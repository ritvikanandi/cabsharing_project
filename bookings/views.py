from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm, BookingForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import createbooking

# Create your views here.
def main(request):
    return render(request, 'bookings/home.html')

def home(request):
    books = createbooking.objects
    return render(request, 'bookings/index.html', {'books': books})


@login_required
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback=form.save(commit=False)
            feedback.user=request.user
            feedback.save()
            return render(request, 'bookings/feedback_submitted.html')

    else:
        form = FeedbackForm()
        return render(request, 'bookings/feedback.html', {'form': form})


@login_required
def create_booking(request):
    if request.method=='POST':
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
<<<<<<< HEAD
            booking.user=request.user

            pickup = booking_form.cleaned_data.get("pickup")
            destination = booking_form.cleaned_data.get("destination")
            if( pickup == destination):
=======
            if(booking.pickup == booking.destination):
>>>>>>> 9707b91aa08f71c60f8b3f3b605d7bd060254610
                return render(request, 'bookings/createbooking.html',{'error':'The pickup location and destination should be different'})
            booking.user = request.user
            booking.save()
            return redirect('bookings')
        else:
            return render(request,'bookings/createbooking.html',{'booking_form':booking_form})
    else:
        booking_form = BookingForm()
        return render(request,'bookings/createbooking.html',{'booking_form':booking_form})
