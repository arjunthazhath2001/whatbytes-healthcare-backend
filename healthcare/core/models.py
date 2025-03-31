from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Patient(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')

    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    date_of_birth=models.DateField()

    gender= models.CharField(max_length=10, choices=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),])
    
    phone= models.CharField(max_length=15)
    address= models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Doctor(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    specialization= models.CharField(max_length=100)
    license_number= models.CharField(max_length=50, unique=True)
    phone= models.CharField(max_length=15)
    email= models.EmailField(unique=True)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.first_name}{self.last_name}"
    

class PatientDoctorMapping(models.Model):
    patient= models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_mappings')
    
    doctor= models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient_mappings')

    assigned_date= models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together= ('patient', 'doctor')

    def __str__(self):
        return f"{self.patient}-{self.doctor}"
