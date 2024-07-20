from django.db import models

from doctorapp.models import registeration
from userapp.models import booking


# Create your models here.
class approval(models.Model):
    books=models.OneToOneField(booking,on_delete=models.CASCADE)
    user = models.OneToOneField(registeration,on_delete=models.CASCADE)
    bkngdate=models.DateField()
    cnsultdate=models.DateTimeField()