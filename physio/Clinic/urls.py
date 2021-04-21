from django.urls import path
from . import views

urlpatterns = [
path('Clinic/Patient/<int:patient_id>',views.ClinicDetailsByPat,name='ClinicDetailsByPatient'),
path('Clinic/<int:clinic_id>',views.clinic_detail,name='clinic_detail'),
path('Clinic',views.ClinicList.as_view(),name='clinic_list'),
]