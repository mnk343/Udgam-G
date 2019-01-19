from django.contrib.auth.models import User
from users.models import CustomUser
from multiselectfield import MultiSelectField
from django.db import models

sex = (
        ('male','male'),
        ('female','female'),
     )

days = (
        ('monday' , 'monday') ,
        ('tuesday' , 'tuesday') ,
        ('wednesday' , 'wednesday') ,
        ('thursday' , 'thursday') ,
        ('friday' , 'friday') ,
        ('saturday' , 'saturday') ,
        ('sunday' , 'sunday') ,
)

class Patient (models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE , null=True)

    name = models.CharField(max_length = 200 , blank = False)
    age = models.IntegerField(default = 18)
    sex = models.CharField(max_length = 100 , choices = sex )

class Doctor(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)


    name = models.CharField(max_length = 200 , blank = False)


class Slot(models.Model):
    day = models.CharField(max_length = 100 ,choices = days , default='monday')
    time = models.IntegerField( blank = False)
    availability = models.IntegerField(default = 0 , blank = False)
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE , null=True)
