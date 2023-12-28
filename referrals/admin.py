from django.contrib import admin
from .models import Person, Doctor, Referral

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Person)
admin.site.register(Referral)
