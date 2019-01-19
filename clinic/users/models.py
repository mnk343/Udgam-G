from django.contrib.auth.models import AbstractUser
from django.db import models

PERSON = (
        ('patient','patient'),
        ('doctor','doctor'),
        ('staff','staff'),
)

class CustomUser(AbstractUser):
    person = models.CharField(max_length=100,choices=PERSON,default='patient')
