from django.contrib import admin
from .models import Patient, Doctor, Referral

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Referral)
