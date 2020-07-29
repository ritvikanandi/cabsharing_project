from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import UserForm, DetailsForm
from .models import Booker
# Create your views here.


def signup(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        details_form = DetailsForm(request.POST)
        if (user_form.is_valid() and details_form.is_valid()):
            user = user_form.save(commit = False)
            user.set_password(user.password)    #returns a user that is not saved in the database yet.
            user.save()

            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password')         #raw passwords are not saved so set_password is necessary
            profile=details_form.save(commit = False)
            profile.user = user

            if request.FILES['dp']:
                profile.dp = request.FILES['dp']

            profile.save()

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'accounts/signup.html', {'error': 'Something went wrong :)'})      #handle the errors

    else:
        user_form = UserForm();
        details_form = DetailsForm();
        return render(request, 'accounts/signup.html', {'user_form': user_form, 'details_form': details_form})

def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'accounts/profile.html', {'user': user})
