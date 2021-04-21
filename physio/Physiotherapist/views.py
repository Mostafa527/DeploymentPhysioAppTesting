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
def physiotheripst_detail(request, physio_id):
    try:
        physiotheripst =Physiotherapist.objects.get(pk=physio_id)
    except Physiotherapist.DoesNotExist:
        return Response({'message': 'The Physiotheripst does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        physiotheripst_serializer = PhysiotherapistSerializer(physiotheripst)
        return Response(physiotheripst_serializer.data)

    elif request.method == 'PUT':
        physiotheripst_data = JSONParser().parse(request)
        physiotheripst_serializer = ClinicSerializer(physiotheripst, data=physiotheripst_data)
        if physiotheripst_serializer.is_valid():
            physiotheripst_serializer.save()
            return Response(physiotheripst_serializer.data)
        return Response(physiotheripst_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        physiotheripst.delete()
        return Response({'message': 'Physiotheripst was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class PhysiotheripstList(APIView):
    def get(self,request):
        physiotherapists = Physiotherapist.objects.all()
        data=PhysiotherapistSerializer(physiotherapists,many=True).data
        return Response(data)
    def post(self,request):
        serializer = PhysiotherapistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def therpyDetailsByPatient(request,patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({'message': 'The Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            physiotherapist=Physiotherapist.objects.get(pk=patient.Physio_Patient.pk)
        except Physiotherapist.DoesNotExist:
            return Response({'message': 'The Physiotherapist does not exist'}, status=status.HTTP_404_NOT_FOUND)
        physiotherapist_serializer = PhysiotherapistSerializer(physiotherapist)
        return Response(physiotherapist_serializer.data)


@api_view(['GET'])
def therpysDetailsByClinic(request,clinic_id):
    try:
        clinic = Clinic.objects.get(pk=clinic_id)
    except Clinic.DoesNotExist:
        return Response({'message': 'The Clinic does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            physiotherapist=clinic.pysio_therpists.all()
        except Physiotherapist.DoesNotExist:
            return Response({'message': 'The Physiotherapist does not exist'}, status=status.HTTP_404_NOT_FOUND)
        physiotherapist_serializer = PhysiotherapistSerializer(physiotherapist,many=True)
        return Response(physiotherapist_serializer.data)
