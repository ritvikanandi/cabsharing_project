from django.contrib import admin
<<<<<<< HEAD
from .models import createbooking
# Register your models here.
=======
from .models import Feedback, createbooking
# Register your models here.
admin.site.register(Feedback)
>>>>>>> 9707b91aa08f71c60f8b3f3b605d7bd060254610
admin.site.register(createbooking)
