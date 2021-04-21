
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from physio.models import *
from physio.serializer import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, patient_id):
    try:
        patient =Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({'message': 'The Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        patient_serializer = PatientSerializer(patient)
        return Response(patient_serializer.data)

    elif request.method == 'PUT':
        patient_data = JSONParser().parse(request)
        patient_serializer = ClinicSerializer(patient, data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return Response(patient_serializer.data)
        return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patient.delete()
        return Response({'message': 'Patient was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class PatientList(APIView):
    def get(self,request):
        patients = Patient.objects.all()
        data=PatientSerializer(patients,many=True).data
        return Response(data)
    def post(self,request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def PatientsDetailsByTherpy(request,physio_id):
    try:
        physiotherapist = Physiotherapist.objects.get(pk=physio_id)
    except Physiotherapist.DoesNotExist:
        return Response({'message': 'The Physiotherapist does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            patient=physiotherapist.patients.all()
        except Patient.DoesNotExist:
            return Response({'message': 'The Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)
        patient_serializer = PatientSerializer(patient,many=True)
        return Response(patient_serializer.data)