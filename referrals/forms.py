from django import forms
from .models import Person, Referral

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth', 'GP']

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
