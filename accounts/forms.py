from django import forms
from django.contrib.auth.models import User
from .models import Booker

HOSTEL_CHOICES = (
    ('brahmaputra','BRAHMAPUTRA'),
    ('dihing', 'DIHING'),
    ('lohit','LOHIT'),
    ('manas','MANAS'),
    ('umiam','UMIAM'),
    ('barak','BARAK'),
    ('kameng', 'KAMENG'),
    ('kapili','KAPILI'),
    ('siang','SIANG'),
    ('dibang','DIBANG'),
    ('disang','DISANG'),
    ('dhansiri', 'DHANSIRI'),
    ('subhansiri','SUBHANSIRI'),
    ('msh','MSH'),
)

GENDERS = (
   ('male', 'MALE'),
   ('female', 'FEMALE'),
)

class UserForm(forms.ModelForm):
    username = forms.CharField(label = "Username")
    email = forms.EmailField(label = "Email")  #add validator for webmail id check
    password = forms.CharField(widget = forms.PasswordInput, label = "Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class DetailsForm(forms.ModelForm):
    hostel = forms.ChoiceField(choices=HOSTEL_CHOICES, required=True)
    gender = forms.ChoiceField(choices=GENDERS, required=True)

    class Meta:
        model = Booker
        fields = ['hostel', 'gender', 'dp']
