from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm, BookingForm, MemberForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import createbooking, Member
from django.contrib import messages
from .filters import BookingFilter


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
                return render(request, 'bookings/createbooking.html',{'error':'The pickup location and destination should be different'})
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
                    return redirect('bookings')
            if (request.user.username == booking.user.username):
                return redirect('bookings')
            if(booking.peopletogether < 4):
                booking.peopletogether += 1
                booking.save()
            member=form.save(commit=False)
            member.booking= booking
            member.user = request.user
            member.save()
            return redirect('bookings')
    else:
        form = MemberForm()
        if(booking.user.username == request.user.username):
            return redirect('bookings')
        else:
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
                return redirect('bookings')
            except Member.DoesNotExist:
                return redirect('bookings')
    else:
        leaveform=MemberForm()
        people=booking.members.all()
        for any in people:
            if(request.user.username == any.user.username):
                return render(request, 'bookings/member_leave.html', {'leaveform':leaveform})

        return redirect('bookings')



def booking_info(request, booking_id):
    booking = get_object_or_404(createbooking, pk=booking_id)
    return render(request, 'bookings/details.html', {'booking': booking})


def filter_bookings(request):
    list = createbooking.objects.all()
    filter = BookingFilter(request.GET, queryset=list)
    return render(request, 'bookings/index.html', {'filter': filter})
