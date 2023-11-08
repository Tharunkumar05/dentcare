from django.contrib import admin
from .models import Patient, Dentist, Registration



admin.site.register(Patient)
admin.site.register(Dentist)
admin.site.register(Registration)
