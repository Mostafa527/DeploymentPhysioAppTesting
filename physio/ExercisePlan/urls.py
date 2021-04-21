from django.urls import path
from . import views

urlpatterns = [

path('ExercisePlan/<int:exerciseplan_id>',views.exerciseplan_detail,name='exerciseplan_detail'),
path('ExercisePlan',views.ExercisePlanList.as_view(),name='exerciseplan_list'),
path('ExercisePlan/Patient/<int:patient_id>',views.ExercisePlanDetailsByPatient,name='ExercisePlanDetailsByPatient'),
]