from django.conf.urls import url
from PatientApp import views

urlpatterns=[
    url(r'^doctor$',views.doctorApi),
    url(r'^doctor/([0-9]+)$',views.doctorApi),

    url(r'^patient$',views.patientApi),
    url(r'^patient/([0-9]+)$',views.patientApi)
    


]