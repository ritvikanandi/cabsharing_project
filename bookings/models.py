from django.db import models
from django.contrib.auth.models import User



class createbooking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    time = models.TimeField(help_text="format (hh:mm:ss)")
    date = models.DateField(help_text="format (yyyy-mm-dd)")
    pickup = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    luggage = models.DecimalField(help_text="Please enter the value in kg maximum upto two decimal places", decimal_places=2, max_digits=5)
    peopletogether = models.IntegerField(default=0)
    budget = models.CharField(max_length=50)
    is_drop = models.BooleanField(default=False)

    def __str__(self):
        return "from " + self.pickup+ " to " + self.destination + " at " + str(self.date) + " " + str(self.time) + "-/-" +str(self.pk)




class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , blank=True)
    details = models.TextField()

    def __str__(self):
        return self.user.username
