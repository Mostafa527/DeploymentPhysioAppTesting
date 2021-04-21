from django.urls import path
from . import views

urlpatterns = [
path('Patient/<int:patient_id>',views.patient_detail,name='patient_detail'),
path('Patient',views.PatientList.as_view(),name='patient_list'),
path('Patient/Physiotherapist/<int:physio_id>',views.PatientsDetailsByTherpy,name='PatientDetailsByTherpy'),
]