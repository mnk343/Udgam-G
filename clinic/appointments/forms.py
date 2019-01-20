from . import models
from django import forms

days = [
        ('Monday' , 'Monday') ,
        ('Tuesday' , 'Tuesday') ,
        ('Wednesday' , 'Wednesday') ,
        ('Thursday' , 'Thursday') ,
        ('Friday' , 'Friday') ,
        ('Saturday' , 'Saturday') ,
        ('Sunday' , 'Sunday') ,
]

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
            'profile_pic'
        ]


class UpdateDoctorDetail(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = [
            'name',
            'age',
            'sex',
            'specialization',
            'contact_no',
            'email_id',
            'qualifications',
            'yearsOfExperience',
            'profile_pic',
        ]

class BookAppointmentForm(forms.Form):
    day=forms.ChoiceField(choices=days)
    time = forms.ChoiceField(choices=[(x, x) for x in range(1, 25)])
