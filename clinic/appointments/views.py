from django.shortcuts import render
from . import models
from . import forms
from django.shortcuts import redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
    if request.user.person=='patient':
        patient = models.Patient.objects.filter(user=request.user)
        if not patient :
            form = forms.UpdatePatientDetail()
            if request.method=='POST' :
                form = forms.UpdatePatientDetail(request.POST)
                if form.is_valid():
                    detail = form.save(commit=False)
                    detail.user = request.user
                    detail.save()
                    #we are getting an error
                return redirect('appointments:dashboard')
            else :
                return render(request,'appointments/UpdatePatientDetail.html', {'form':form , 'patient':request.user.username} )
        else:
            patient = models.Patient.objects.get(user=request.user)
            # forms = models.ApplyLeave.objects.filter(patient=patient)
            return render(request,'appointments/PatientDashboard.html',{'user':request.user , 'patient':patient})

    elif request.user.person=='doctor':
        doctor = models.Doctor.objects.filter(user=request.user)
        if not doctor :
            form = forms.UpdateDoctorDetail()
            if request.method=='POST' :
                form = forms.UpdateDoctorDetail(request.POST)
                if form.is_valid():
                    detail = form.save(commit=False)
                    detail.user = request.user
                    detail.save()
                    #we are getting an error
                return redirect('appointments:dashboard')
            else :
                return render(request,'appointments/UpdateDoctorDetail.html', {'form':form , 'doctor':request.user.username} )
        else:
            doctor = models.Doctor.objects.get(user=request.user)
            return render(request,'appointments/DoctorDashboard.html',{'user':request.user , 'doctor':doctor})

def UpdateProfile(request):

    patient = get_object_or_404(models.Patient, pk=pk)

    form = forms.UpdatePatientDetail(instance=patient)

    if request.user.person == 'patient':
        if request.method == 'POST':
            form = forms.UpdatePatientDetail(instance=patient, data=request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(patient.get_absolute_url())

        return render(request, 'appointments/UpdatePatientDetail.html', {'form':form, 'patient':patient})

    elif request.user.person == 'patient':
        doctor = get_object_or_404(models.Doctor, pk=pk)
        form = forms.UpdateDoctorDetail(instance=doctor)

        if request.method == 'POST':
            form = forms.UpdateDoctorDetail(instance=doctor, data=request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(doctor.get_absolute_url())

        return render(request, 'appointments/UpdateDoctorDetail.html', {'form':form, 'doctor':doctor})
