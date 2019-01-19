from . import models
from django import forms

class UpdatePatientDetail(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = [
            'name',
            'age',
            'sex',
            'blood_group',
            'contact_no',
            'email_id',
        ]


class UpdateDoctorDetail(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = [
            'name',
            'age',
            'sex',
            'blood_group',
            'contact_no',
            'email_id',
        ]
