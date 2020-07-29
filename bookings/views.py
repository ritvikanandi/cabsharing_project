from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import createbooking
from .forms import BookingForm
# Create your views here.
def home(request):
    return render(request, 'bookings/home.html')

@login_required(login_url="/accounts/signup")
def createbooking(request):
    if request.method=='POST':
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user=request.user
            pickup = booking_form.cleaned_data.get("pickup")
            destination = booking_form.cleaned_data.get("destination")
            if pickup == destination:
                return render(request, 'bookings/createbooking.html',{'error':'The pickup location and destination should be different'})
            else:
                booking.save()
                return redirect('home')
        else:
            return render(request,'bookings/createbooking.html',{'booking_form':booking_form})
    else:
        booking_form = BookingForm()
        return render(request,'bookings/createbooking.html',{'booking_form':booking_form})
