from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view


"""
@api_view(['POST', 'PUT', 'DELETE'])
def clinic_list(request):
     if request.method == 'POST':
        clinic_data = JSONParser().parse(request)
        clinic_serializer = ClinicSerializer(data=clinic_data)
        if clinic_serializer.is_valid():
            clinic_serializer.save()
            return JsonResponse(clinic_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(clinic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""





