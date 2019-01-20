from django.shortcuts import render
from . import models
from . import forms
from django.shortcuts import redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

def homepage(request):
    return render(request , 'index.html')

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
            apps = models.Appointment.objects.filter(patient=patient)
            apps_new = apps.filter(cancelled=False)

            cancelled = apps.filter(cancelled=True)
            return render(request,'appointments/PatientDashboard.html',{'user':request.user , 'patient':patient, 'apps':apps_new , 'cancelled':cancelled })

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
            apps_all = models.Appointment.objects.filter(doctor=doctor)
            apps = apps_all.filter(cancelled=False)
            # cancelled = models.Appointment.objects.filter(cancelled=True)

            return render(request,'appointments/DoctorDashboard.html',{'user':request.user , 'doctor':doctor, 'apps':apps})

def UpdateProfile(request , pk):

    if request.user.person == 'patient':
        patient = get_object_or_404(models.Patient, pk=pk)
        form = forms.UpdatePatientDetail(instance=patient)

        if request.method == 'POST':
            form = forms.UpdatePatientDetail(instance=patient, data=request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(patient.get_absolute_url())

        return render(request, 'appointments/UpdatePatientDetail.html', {'form':form, 'patient':patient})

    elif request.user.person == 'doctor':
        doctor = get_object_or_404(models.Doctor, pk=pk )
        form = forms.UpdateDoctorDetail(instance=doctor)

        if request.method == 'POST':
            form = forms.UpdateDoctorDetail(instance=doctor, data=request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(doctor.get_absolute_url())

        return render(request, 'appointments/UpdateDoctorDetail.html', {'form':form, 'doctor':doctor})


def CreateSlots(request, pk):
    if request.user.person=='doctor':
        doctor = get_object_or_404(models.Doctor, pk=pk)

        days_week = ['Monday' , 'Tuesday' , 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        times = []
        working_time = [11,12,15,16,17,18]

        for i in range(1,25):
            times.append(i)

        for i in days_week:
            for j in times:
                ctr=0
                if j in working_time:
                    ctr=3
                models.Slot.objects.create(
        					day = i,
        					time = j,
        					availability = ctr,
        					doctor = doctor,
        				)

        return redirect('appointments:dashboard')
    else :
        raise HttpResponse('<h1>no access</h1>')

def BookAppointment(request):
    if request.user.person=='patient':
        form = forms.BookAppointmentForm()
        if request.method == 'POST':
            form = forms.BookAppointmentForm(request.POST)
            day = request.POST['day']
            time = int(request.POST['time'])
            if form.is_valid():
                context={'day':day, 'time':time}
                return ShowAvailable(request , context)
        else:
            return render(request, 'appointments/BookAppointment.html', {'form':form})
    else :
        raise HttpResponse('<h1>no access</h1>')


def ShowAvailable(request , context):

    day = context['day']
    time = context['time']

    all_doctors = models.Doctor.objects.all()
    context['doctors']=[]

    for i in all_doctors:

        for j in i.slot_set.all():

            if j.availability>0:
                if j.day == day and j.time == time :
                    context['doctors'].append( ( i , j ) )

    return render(request, 'appointments/ShowAvailable.html' , context)

def bookSlot(request,pk):
    slot = models.Slot.objects.get(pk=pk)
    slot.availability -= 1
    slot.save()
    patient = models.Patient.objects.get(user=request.user)
    models.Appointment.objects.create(
                day = slot.day,
                time = slot.time,
                patient = patient,
                doctor = slot.doctor,
            )

    return redirect('appointments:dashboard')


def cancelAppointment(request, pk):
    app = models.Appointment.objects.get(pk=pk)
    doctor = app.doctor
    patient = app.patient
    day = app.day
    time = app.time
    doc_slots = doctor.slot_set.all()
    doc_slots = doc_slots.filter(day=day)
    doc_slot = doc_slots.get(time=time)
    doc_slot.availability +=1
    doc_slot.save()
    app.cancelled = True
    app.save()
    return redirect('appointments:dashboard')

def deleteAppointment(request, pk):
    app = models.Appointment.objects.get(pk=pk)
    app.delete()
    return redirect('appointments:dashboard')
