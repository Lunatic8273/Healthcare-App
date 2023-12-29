from django import forms
from .models import Patient, Referral, Doctor

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['user', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'GP']

class PatientEditForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth']

class DoctorAddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth']

class PatientAddReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['referral_date', 'referral_reason', 'note', 'document']

class DoctorAddReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['patient', 'referral_date', 'referral_reason', 'note', 'document']

class GlobalReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['patient', 'referrer', 'referral_date', 'referral_reason', 'note', 'document']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['portrait_img', 'first_name', 'last_name', 'medical_center']
