from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PatientApp.models import doctor,Patients
from PatientApp.serializers import DoctorSerializer,PatientsSerializer

# Create your views here.

@csrf_exempt
def doctorApi(request,id=0):
    if request.method=='GET':
        medecin=doctor.objects.all()
        medecin_serializer=DoctorSerializer(medecin,many=True)
        return JsonResponse(medecin_serializer.data,safe=False)
    elif request.method=='POST':
        medecin_data=JSONParser().parse(request)
        medecin_serializer=DoctorSerializer(data=medecin_data)
        if medecin_serializer.is_valid():
            medecin_serializer.save()
            return JsonResponse("Added Successfully" ,safe=False)
        return JsonResponse("Failed Adding",safe=False)
    elif request.method=="PUT":
        medecin_data=JSONParser().parse(request)
        med=doctor.objects.get(DoctorId=medecin_data['DoctorId'])
        medecin_serializer=DoctorSerializer(med,data=medecin_data)
        if medecin_serializer.is_valid():
            medecin_serializer.save()
            return JsonResponse("Doctor Updated",safe=False)
        return JsonResponse("Failed",safe=False)
    elif request.method=='DELETE':
        med=doctor.objects.get(DoctorId=id)
        med.delete()
        return JsonResponse("Deleted",safe=False)

@csrf_exempt
def patientApi(request,id=0):
    if request.method=='GET':
        patient=Patients.objects.all()
        patient_serializer=PatientsSerializer(patient,many=True)
        return JsonResponse(patient_serializer.data,safe=False)
    elif request.method=='POST':
        patient_data=JSONParser().parse(request)
        patient_serializer=PatientsSerializer(data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse("Added patient Successfully" ,safe=False)
        return JsonResponse("Failed Adding patient",safe=False)
    elif request.method=="PUT":
        patient_data=JSONParser().parse(request)
        patient=doctor.objects.get(DoctorId=patient_data['PatientId'])
        patient_serializer=PatientsSerializer(patient,data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse("Patient Updated",safe=False)
        return JsonResponse("Failed",safe=False)
    elif request.method=='DELETE':
        patient=doctor.objects.get(patientId=id)
        patient.delete()
        return JsonResponse("Deleted",safe=False)


