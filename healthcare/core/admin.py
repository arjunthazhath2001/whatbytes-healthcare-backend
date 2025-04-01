from django.contrib import admin
from .models import Patient, Doctor, PatientDoctorMapping

# Register models with the admin site
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PatientDoctorMapping)