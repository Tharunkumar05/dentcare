from django.db import models
from django.contrib.auth.models import User  
import datetime
import os

from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    # Other patient-related fields such as medical history can be added here

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Dentist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    # Other dentist-related fields such as specialization can be added here

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Registration(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    registration_date=models.DateField(null=False,blank=False)
    patient_name=models.CharField(max_length=255,null=False,blank=False)
    gender=models.CharField(max_length=255,null=False,blank=False)
    phone_number = models.CharField(max_length=255,null=False,blank=False)
    email=models.CharField(max_length=255,null=False,blank=False)
    city=models.CharField(max_length=255,null=False,blank=False)

    def __str__(self):
        return f"{self.registration_date}"