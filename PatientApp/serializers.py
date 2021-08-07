from django.db.models import fields
from rest_framework import serializers
from PatientApp.models import doctor,Patients

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=doctor
        fields=('DoctorId','DoctorName','DoctorPass')

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields=('PatientId','PatientName','SessionNumber','ConsultationDate','ConsultationVideo','HeadMovementData','EyeMovementRecord','DiagnosisType','DoctorComment')