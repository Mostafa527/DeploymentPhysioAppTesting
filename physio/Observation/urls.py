
from django.urls import path
from . import views

urlpatterns = [

path('Observation/Session/<int:session_id>',views.ObservationDetailsBySession,name='ObservationDetailsBySession'),
path('Observation/<int:observation_id>',views.observation_detail,name='observation_detail'),
path('Observation',views.ObservationList.as_view(),name='observation_list'),
]