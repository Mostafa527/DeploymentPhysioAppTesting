from django.urls import path
from . import views

urlpatterns = [

path('Session/ExercisePlan/<int:exerciseplan_id>',views.SessionByExercisePlan,name='SessionByExercisePlan'),
path('Session/<int:session_id>',views.session_detail,name='session_detail'),
path('Session',views.SessionList.as_view(),name='session_list'),
]