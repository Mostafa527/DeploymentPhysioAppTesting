from django.urls import path
from . import views

urlpatterns = [
path('Admin/<int:admin_id>',views.admin_detail,name='admin_detail'),
path('_Admin',views.adminList.as_view(),name='admin_list'),
]