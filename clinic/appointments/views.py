from django.shortcuts import render

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
                return render(request,'appointments/PatientDetail.html', {'form':form , 'patient':request.user.username} )
        else:
            patient = models.Patient.objects.get(user=request.user)
            # forms = models.ApplyLeave.objects.filter(patient=patient)
            return render(request,'appointments/dashboard.html',{'user':request.user , 'patient':patient})

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
                return render(request,'appointments/doctor_update_detail.html', {'form':form , 'doctor':request.user.username} )
        else:
            doctor = models.Doctor.objects.get(user=request.user)
            return render(request,'leave_portal/doctor_dashboard.html',{'user':request.user , 'doctor':doctor})
