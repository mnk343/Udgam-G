from django.contrib.auth.models import User
from users.models import CustomUser
from multiselectfield import MultiSelectField
from django.db import models
from django.shortcuts import reverse

sex = (
        ('male','male'),
        ('female','female'),
     )

blood_group = (
        ('A+','A+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('O+','O+'),
        ('A-','A-'),
        ('B-','B-'),
        ('AB-','AB-'),
        ('O-','O-'),
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
    profile_pic = models.ImageField(upload_to='patient/', default = 'dp.png')

    name = models.CharField(max_length = 200 , blank = False)
    age = models.IntegerField(default = 18)
    sex = models.CharField(max_length = 100 , choices = sex )
    blood_group = models.CharField(max_length=10,  choices = blood_group )
    contact_no  = models.IntegerField()
    email_id = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('appointments:dashboard')
    def __str__(self):
        return self.name

class Doctor(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 200 , blank = False)
    age = models.IntegerField(default = 18)
    profile_pic = models.ImageField(upload_to='doctor/', default = 'dp.png')

    sex = models.CharField(max_length = 100 , choices = sex )
    specialization = models.CharField(max_length=100, blank = True)
    qualifications = models.CharField(max_length=100 , blank = True)
    yearsOfExperience = models.IntegerField(default = 0)
    contact_no  = models.IntegerField()
    email_id = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('appointments:dashboard')
    def __str__(self):
        return self.name

class Slot(models.Model):
    day = models.CharField(max_length = 100 ,choices = days , default='monday')
    time = models.IntegerField( blank = False)
    availability = models.IntegerField(default = 0 , blank = False)
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.doctor.name +  " " + self.day + " " + str(self.time)

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE , null=True)
    patient = models.ForeignKey(Patient , on_delete=models.CASCADE , null=True)
    day = models.CharField(max_length = 100 ,choices = days , default='monday')
    time = models.IntegerField( blank = False)
    cancelled = models.BooleanField( default = False)
    def __str__(self):
        return self.doctor.name +  " " + self.patient.name + " " + self.day
