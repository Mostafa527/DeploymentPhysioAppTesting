from django.urls import path
from . import views

urlpatterns = [

path('Game',views.GametList.as_view(),name='game_list'),

]