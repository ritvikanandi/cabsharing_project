from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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

class Booker(models.Model):                                               #model for the cab booker
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hostel = models.CharField(max_length=11, choices=HOSTEL_CHOICES, default='brahmaputra')
    gender = models.CharField(max_length=6, choices=GENDERS, default='male')
    dp = models.ImageField(default='default-pic.jpg', blank='True', upload_to = 'user_dp')

    def __str__(self):
       return self.user.username
