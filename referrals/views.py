from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, Referral, Doctor
from .forms import PatientForm, PatientEditForm, DoctorAddReferralForm, GlobalReferralForm, PatientAddReferralForm, DoctorForm, DoctorAddPatientForm
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse
import os

#---------LOGIN---------
@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to the home page or any other desired page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'referrals/home.html')

#---------PAGES---------
def home(request):
    return render(request, 'referrals/home.html')

def about_page(request):
    return render(request, 'about.html')

def our_staff(request):
    doctors = Doctor.objects.all()
    return render(request, 'our_staff.html', {'doctors':doctors})

#---------PATIENT PROFILE PAGE---------
def patient_profile(request):
    patient = get_object_or_404(Patient, user=request.user)
    referrals = Referral.objects.filter(patient=patient)
    return render(request, 'patients/patient_profile.html', {'patient':patient, 'referrals': referrals})

#---------patient---------
@login_required
def patient_cancel(request):
    return render(request, 'referrals/patient_list.html')    

@login_required
def my_patient_list(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    patients = patient.objects.filter(GP=doctor.id)
    return render(request, 'referrals/my_patient_list.html', {'doctor':doctor, 'patients': patients})

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'referrals/patient_list.html', {'patients': patients})

@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    referrals = Referral.objects.filter(patient=patient)
    return render(request, 'referrals/patient_detail.html', {'patient': patient, 'referrals': referrals})

@login_required
def patient_new(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm()
    return render(request, 'referrals/patient_new.html', {'form': form})

@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'referrals/patient_edit.html', {'form': form, 'patient': patient})

@login_required
def patient_patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientEditForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientEditForm(instance=patient)
    return render(request, 'referrals/patient_edit.html', {'form': form, 'patient': patient})
 
@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('patient_list')

#---------DOCTOR---------
def is_doctor(user):
    return user.groups.filter(name='Doctors').exists()

@login_required
def doctor_add_patient_new(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    if request.method == "POST":
        form = DoctorAddPatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.GP = doctor
            patient.save()
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = DoctorAddPatientForm()
    return render(request, 'referrals/patient_new.html', {'form': form})

def doctor_page(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'referrals/doctor_page.html',{'doctor': doctor})

@login_required
def my_doctor_page(request):
    doctors = Doctor.objects.all()
    is_dr = False
    for doctor in doctors:
        if doctor.user_id == request.user.id: 
            is_dr = True
            continue
    if is_dr == False:
        return redirect('add_doctor')
    elif is_dr == True:
        doctor = get_object_or_404(Doctor, user_id=request.user.id)
        return render(request, 'referrals/doctor_page.html',{'doctor': doctor})

@login_required
def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect('doctor_page', pk=doctor.pk)
    else:
        form = DoctorForm()
    return render(request, 'referrals/doctor_new.html', {'form': form})

@login_required
def edit_doctor(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect('my_doctor_page')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'referrals/doctor_edit.html', {'form': form, 'doctor':doctor})

#---------REFERRAL---------
@login_required
def referral_list(request):  
    referrals = Referral.objects.all()
    return render(request, 'referrals/referral_list.html', {'referrals': referrals})

@login_required
def my_referral_list(request):  
    doctor = get_object_or_404(Doctor, user=request.user)
    referrals = Referral.objects.filter(referrer=doctor.id)
    return render(request, 'referrals/my_referral_list.html', {'doctor':doctor,'referrals': referrals})

@login_required
def referral_detail(request, referral_id):
    referral = get_object_or_404(Referral, id=referral_id)
    patient = get_object_or_404(patient, id=referral.patient.id)
    return render(request, 'referrals/referral_detail.html', {'patient': patient, 'referral': referral})
    
@login_required
def view_document(request, referral_id):
    referral = get_object_or_404(Referral, id=referral_id)
    if referral.document:
        with open(referral.document.path, 'rb') as document_file:
            response = HttpResponse(document_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename={referral.document.name}'
            return response
    else:
        return HttpResponse("Document not found", status=404)


@login_required
def patient_referral_new(request, patient_id):
    doctor = get_object_or_404(Doctor, user=request.user)
    patient = get_object_or_404(patient, id=patient_id)
    if request.method == "POST":
        form = PatientAddReferralForm(request.POST)
        if form.is_valid():
            referral = form.save(commit=False)
            referral.referrer = doctor
            referral.patient = patient
            referral.save()
            return render(request, 'referrals/referral_detail.html',{'patient': patient, 'referral':referral})
    else:
        form = PatientAddReferralForm()
    return render(request, 'referrals/referral_new.html', {'form': form, 'patient': patient})

@login_required
def doctor_referral_new(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    if request.method == "POST":
        form = DoctorAddReferralForm(request.POST)
        if form.is_valid():
            referral = form.save(commit=False)
            referral.referrer = doctor
            patient = referral.patient
            referral.save()
            return render(request, 'referrals/referral_detail.html',{'patient': patient, 'referral':referral})
    else:
        form = DoctorAddReferralForm()
    return render(request, 'referrals/referral_new.html', {'form': form})

@login_required
def global_referral_new(request):
    if request.method == "POST":
        form = GlobalReferralForm(request.POST)
        if form.is_valid():
            referral = form.save(commit=False)
            patient = referral.patient
            referral.save()
            return render(request, 'referrals/referral_detail.html',{'patient':patient,'referral':referral})
    else:
        form = GlobalReferralForm()
    return render(request, 'referrals/referral_new.html', {'form': form})

@login_required
def global_referral_edit(request, patient_id, referral_id):
    referral = get_object_or_404(Referral, id=referral_id, patient__id=patient_id)
    if request.method == "POST":
        form = GlobalReferralForm(request.POST, request.FILES, instance=referral)
        if form.is_valid():
            referral = form.save(commit=False)
            referral.patient = referral.patient
            referral.save()
            return redirect('referral_detail', referral_id=referral.pk)
    else:
        form = GlobalReferralForm(instance=referral)
    return render(request, 'referrals/referral_edit.html', {'form': form, 'patient':referral.patient, 'referral':referral})

@login_required
def referral_delete(request, patient_id, referral_id):
    referral = get_object_or_404(Referral, id=referral_id, patient__id=patient_id)
    referral.delete()
    return redirect('referral_list')

