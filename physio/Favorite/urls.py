from django.urls import path
from . import views

urlpatterns = [
path('Favorite/<int:patient_id>',views.FavoriteByPatient,name='FavoriteByPatient'),
path('Favorite/Physiotheripst/<int:physio_id>',views.FavoriteByPhysiotheripst,name='FavoriteByPhysiotheripst'),
path('Favorite',views.FavoriteList.as_view(),name='favorite_list'),
]