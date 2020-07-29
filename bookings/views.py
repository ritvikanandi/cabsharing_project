from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'bookings/home.html')

@login_required
def bookings(request):
    return render(request, 'bookings/index.html')


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
