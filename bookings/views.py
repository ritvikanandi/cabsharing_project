from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm, BookingForm, MemberForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import createbooking, Member
from django.contrib import messages
import datetime
from .filters import BookingFilter
from accounts.models import Booker


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

            if(booking.pickup == booking.destination):
                messages.error(request,  "The pickup location and destination should be different!")
                return redirect('bookings')
            booking.user = request.user
            booking.save()
            return redirect('bookings')
        else:
            return render(request,'bookings/createbooking.html',{'booking_form':booking_form})
    else:
        booking_form = BookingForm()
        return render(request,'bookings/createbooking.html',{'booking_form':booking_form})

@login_required
def join_booking(request, booking_id):
    booking = get_object_or_404(createbooking, pk=booking_id)
    if request.method == 'POST':
        form=MemberForm(request.POST)
        if form.is_valid():
            people=booking.members.all()
            for any in people:
                if(request.user.username == any.user.username):
                    messages.error(request, "You are already a member of this booking!")
                    return redirect('bookings')
            if (request.user.username == booking.user.username):
                messages.error(request, "You are the creator of this booking!")
                return redirect('bookings')
            if(booking.peopletogether < 4):
                booking.peopletogether += 1
                booking.save()
            if(booking.gender_choice=='boys only'):
                if(request.user.booker.gender == 'female'):
                    messages.error(request,  "Girls can't join BOYS ONLY bookings!")
                    return redirect('bookings')

            if(booking.gender_choice=='girls only'):
                if(request.user.booker.gender == 'male'):
                    messages.error(request,  "Boys can't join  GIRLS ONLY bookings!")
                    return redirect('bookings')

            member=form.save(commit=False)
            member.booking= booking
            member.user = request.user
            member.save()
            return render(request, "bookings/home.html", {'succ': 'Booking joined successfully!'})
    else:
        form = MemberForm()
        if(booking.user.username == request.user.username):
            messages.error(request, "You are the booking creator!")
            return redirect('bookings')

        else:
            if(booking.gender_choice=='boys only'):
                if(request.user.booker.gender == 'female'):
                    messages.success(request,  "Girls can't join BOYS ONLY bookings!")
                    return redirect('bookings')

            if(booking.gender_choice=='girls only'):
                if(request.user.booker.gender == 'male'):
                    messages.error(request,  "Boys can't join GIRLS ONLY bookings!")
                    return redirect('bookings')
            return render(request, 'bookings/member_join.html', {'form':form})


@login_required
def leave_booking(request, booking_id):
    booking=get_object_or_404(createbooking, pk=booking_id)
    if request.method=='POST':
        leaveform=MemberForm(request.POST)
        if leaveform.is_valid():
            try:
                member=booking.members.get(user=request.user)
                member.delete()
                if(booking.peopletogether > 0):
                    booking.peopletogether -= 1
                    booking.save()
                return render(request, "bookings/home.html", {'succ': 'Booking left!'})
            except Member.DoesNotExist:
                return redirect('bookings')
    else:
        leaveform=MemberForm()
        people=booking.members.all()
        for any in people:
            if(request.user.username == any.user.username):
                return render(request, 'bookings/member_leave.html', {'leaveform':leaveform})
        if(booking.user.username == request.user.username):
            messages.error(request, "You need to delete this booking!")
            return redirect('bookings')
        messages.error(request, "You are not a member of this booking!")
        return redirect('bookings')

def booking_info(request, booking_id):
    booking = get_object_or_404(createbooking, pk=booking_id)
    return render(request, 'bookings/details.html', {'booking': booking})

@login_required
def update_booking(request, booking_id):
    booking = get_object_or_404(createbooking, pk=booking_id)
    if request.method=='POST':
        booking_form=BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form=booking_form.save(commit=False)
            if(booking_form.date <datetime.date.today()):
                messages.error(request, "Invalid Date!")
                return redirect('bookings')
            if (booking.user == request.user):
                booking=createbooking.objects.get(pk=booking_id)
                booking.pickup=booking_form.pickup
                booking.destination=booking_form.destination
                booking.date=booking_form.date
                booking.time=booking_form.time
                booking.budget=booking_form.budget
                booking.luggage=booking_form.luggage
                booking.peopletogether=booking_form.peopletogether
                booking.save()
                return render(request, bookings/home.html, {'succ':'Booking updated successfully!'})
            return render(request, "bookings/update.html", {'booking_form':booking_form})
    else:
        booking_form=BookingForm()
        if(booking.user == request.user):
            return render(request, "bookings/update.html", {'booking_form':booking_form})
        else:
            messages.error(request, 'You cannot update this booking!')
            return redirect('bookings')

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(createbooking, pk=booking_id)
    if request.method=='POST':
        if(booking.user == request.user):
            booking.delete()
            return redirect('bookings')
        else:
            messages.error(request, 'You cannot delete this booking!')
            return redirect('bookings')
    else:
        return render(request, 'bookings/delete.html')

    return redirect('bookings')


def filter_bookings(request):
    list = createbooking.objects.all()
    filter = BookingFilter(request.GET, queryset=list)
    return render(request, 'bookings/index.html', {'filter': filter})
