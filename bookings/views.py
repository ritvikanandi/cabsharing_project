from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm, BookingForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import createbooking
from django.views.generic import CreateView , ListView, UpdateView , DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
import datetime
from django.utils import timezone


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
            booking.user=request.user
            pickup = booking_form.cleaned_data.get("pickup")
            destination = booking_form.cleaned_data.get("destination")
            if( pickup == destination):
                return render(request, 'bookings/createbooking.html',{'error':'The pickup location and destination should be different'})
            else:
                booking.save()
                return redirect('/bookings/' + str(booking.id))
        else:
            return render(request,'bookings/createbooking.html',{'booking_form':booking_form})
    else:
        booking_form = BookingForm()
        return render(request,'bookings/createbooking.html',{'booking_form':booking_form})



@login_required
def update_booking(request, booking_id):
    if request.method=='POST':
        booking_form=BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form=booking_form.save(commit=False)

            if(booking_form.date <datetime.date.today()):
                return redirect('bookings:update')
            else:

                booking=createbooking.objects.get(pk=pk)
                booking.pickup=booking_form.pickup
                booking.destination=booking_form.destination
                booking.date=booking_form.date
                booking.time=booking_form.time
                booking.budget=booking_form.budget
                booking.luggage=booking_form.luggage
                booking.peopletogether=booking_form.peopletogether
                booking.max=booking_form.max
                booking.save()
                return redirect('home')
    else:
        obj=get_object_or_404(createbooking, pk=booking_id)
        booking_form=BookingForm( instance=obj)
        return render (request, "bookings/update.html", {'booking_form':booking_form})

def detail(request, booking_id):
    booking = get_object_or_404(createbooking, pk=booking_id)
    return render(request, 'bookings/detail.html',{'booking':booking})

@login_required
def join(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(createbooking, pk=booking_id)
        booking.members_total += 1
        booking.save()
        return redirect('/bookings/' + str(booking.id))

@login_required
def leave(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(createbooking, pk=booking_id)
        booking.members_total -= 1
        booking.save()
        return redirect('/bookings/' + str(booking.id))
