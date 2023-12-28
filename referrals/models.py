from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    medical_center = models.CharField(max_length=100)
    portrait_img = models.ImageField(null=True, upload_to ='uploads/', blank=True) 

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    GP = models.ForeignKey(Doctor, default=None,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Referral(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    referrer = models.ForeignKey(Doctor, default=None, on_delete=models.CASCADE)
    referral_date = models.DateField()
    referral_reason = models.CharField(max_length=255)
    note = models.TextField()
    document = models.FileField(upload_to='documents/', blank=True)

    def __str__(self):
        return f'Referral for {self.person} on {self.referral_date}'

