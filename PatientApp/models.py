from django.db import models

# Create your models here.

class doctor(models.Model):
    DoctorId = models.AutoField(primary_key=True)
    DoctorName = models.CharField(max_length=500)
    DoctorPass = models.CharField(max_length=500)


class Patients(models.Model):
    PatientId = models.AutoField(primary_key=True)
    PatientName = models.CharField(max_length=500)
    SessionNumber = models.CharField(max_length=500)
    ConsultationDate = models.DateField()
    ConsultationVideo = models.CharField(max_length=500)
    HeadMovementData = models.CharField(max_length=500)
    EyeMovementRecord = models.CharField(max_length=500)
    DiagnosisType = models.CharField(max_length=500)
    DoctorComment = models.CharField(max_length=500)
    
    
