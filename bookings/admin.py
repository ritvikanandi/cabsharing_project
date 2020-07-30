from django.contrib import admin

from .models import createbooking
# Register your models here.
from .models import Feedback, createbooking
# Register your models here.
admin.site.register(Feedback)
admin.site.register(createbooking)
