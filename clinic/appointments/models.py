from django.db import models

sex = (
        ('male','male'),
        ('female','female'),
     )

class Patient (models.Model):
    name = models.CharField(max_length = 200 , blank = False)
    age = models.IntegerField(default = 18)
    sex = models.CharField(max_length = 100 , choices = sex )

class Doctor(models.Model):
    name = models.CharField(max_length = 200 , blank = False)
    # slot = models.()


class Slot(models.Model):
    # day = models.CharField(choices = days)
    time = models.IntegerField( blank = False)
    availability = models.IntegerField(default = 0 , blank = False)
    # doctor = models.()
