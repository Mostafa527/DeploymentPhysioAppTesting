from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from physio.models import *
from physio.serializer import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view


class ClinicList(APIView):
    def get(self,request):
        boards = Clinic.objects.all()
        data=ClinicSerializer(boards,many=True).data
        return Response(data)
    def post(self,request):
        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def clinic_detail(request, clinic_id):
    try:
        clinic =Clinic.objects.get(pk=clinic_id)
    except Clinic.DoesNotExist:
        return Response({'message': 'The Clinic does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        clinic_serializer = ClinicSerializer(clinic)
        return Response(clinic_serializer.data)

    elif request.method == 'PUT':
        clinic_data = JSONParser().parse(request)
        clinic_serializer = ClinicSerializer(clinic, data=clinic_data)
        if clinic_serializer.is_valid():
            clinic_serializer.save()
            return Response(clinic_serializer.data)
        return Response(clinic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        clinic.delete()
        return Response({'message': 'Clinic was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def ClinicDetailsByPat(request,patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({'message': 'The Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            clinic=Clinic.objects.get(pk=patient.Physio_Patient.Clinic_Physio.pk)
        except Clinic.DoesNotExist:
            return Response({'message': 'The Clinic does not exist'}, status=status.HTTP_404_NOT_FOUND)
        clinic_serializer = ClinicSerializer(clinic)
        return Response(clinic_serializer.data)


