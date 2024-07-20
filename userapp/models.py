from django.db import models
from doctorapp.models import registeration,schedule
# Create your models here.
class booking(models.Model):
    user = models.OneToOneField(registeration,on_delete=models.CASCADE)
    doctors = models.ManyToManyField(schedule)
    date=models.DateField(auto_now=True)
class bookingitem(models.Model):
    book = models.ForeignKey(booking, on_delete=models.CASCADE)
    sch = models.ForeignKey(schedule, on_delete=models.CASCADE)
