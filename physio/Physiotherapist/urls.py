from django.urls import path
from . import views

urlpatterns = [
path('Physiotherapist/<int:physio_id>',views.physiotheripst_detail,name='physio_detail'),
path('Physiotherapist',views.PhysiotheripstList.as_view(),name='physioList'),
path('Physiotherapist/Patient/<int:patient_id>',views.therpyDetailsByPatient,name='TherpyDetailsByPatient'),
path('Physiotherapist/Clinic/<int:clinic_id>',views.therpysDetailsByClinic,name='TherpyDetailsByClinic'),
]