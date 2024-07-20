
from django.db import models
class department(models.Model):
    dept_name=models.CharField(max_length=200)
    def __str__(self):
          return '{}'.format(self.dept_name)
# Create your models here.
class medicine(models.Model):

    name=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    price=models.IntegerField()

class position(models.Model):

    job=models.CharField(max_length=200)
    def __str__(self):
          return '{}'.format(self.job)
class staff(models.Model):
    username=models.CharField(max_length=200)
    staffposition=models.ForeignKey(position,on_delete=models.CASCADE)
class registeration(models.Model):
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    dob=models.DateField()
    phonenum=models.IntegerField()
    adrs=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    mail = models.EmailField()
    pwd=models.CharField(max_length=200)
    image=models.ImageField()
    last_login = models.DateTimeField(auto_now=True)
    usertype=models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.name)
class prescription(models.Model):
    presc_name= models.OneToOneField(registeration,on_delete=models.CASCADE)
    presc_med=models.ForeignKey(medicine,on_delete=models.CASCADE)
    presc_det=models.CharField(max_length=200)
    presc_num=models.IntegerField(default=1)
class schedule(models.Model):
    docname=models.CharField(max_length=200,null=True)
    docimage = models.ImageField()
    docdepartment=models.ForeignKey(department,on_delete=models.CASCADE)
    workingtime=models.CharField(max_length=200)
    numoftickets=models.PositiveIntegerField()

    def __str__(self):
        return '{}'.format(self.docname)

class labtest(models.Model):
    testname=models.CharField(max_length=200)
    price=models.IntegerField()
    def __str__(self):
        return '{}'.format(self.testname)
class userdiaganosis(models.Model):
    diaganosis_name = models.OneToOneField(registeration, on_delete=models.CASCADE)
    test=models.ForeignKey(labtest,on_delete=models.CASCADE)
    value=models.IntegerField(default=0)


# Create your models here.