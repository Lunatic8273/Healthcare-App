from django import forms
from .models import Person, Referral, Doctor

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['user', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'GP']

class PatientEditForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth']

class DoctorAddPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth']

class PatientAddReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['referral_date', 'referral_reason', 'note', 'document']

class DoctorAddReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['person', 'referral_date', 'referral_reason', 'note', 'document']

class GlobalReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['person', 'referrer', 'referral_date', 'referral_reason', 'note', 'document']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['portrait_img', 'first_name', 'last_name', 'medical_center']
