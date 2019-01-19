from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Doctor)
admin.site.register(models.Patient)
admin.site.register(models.Slot)
admin.site.register(models.Appointment)
