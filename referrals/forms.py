from django import forms
from .models import Person, Referral

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth', 'GP']

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['referral_date', 'referrer', 'referral_reason', 'note', 'document']
