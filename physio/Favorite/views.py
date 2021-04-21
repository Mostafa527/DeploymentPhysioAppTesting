
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from physio.models import *
from physio.serializer import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view


@api_view(['GET'])
def FavoriteByPatient(request,patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({'message': 'The Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            favorite=patient.Patient_Fav.all()
            pat = Patient.objects.get(pk=favorite[0].Patient_Favorite.pk)
        except Favorite.DoesNotExist:
            return Response({'message': 'No Favorite Existed'}, status=status.HTTP_404_NOT_FOUND)

        favorite_serializer = PatientSerializer(pat)
        return Response(favorite_serializer.data)

@api_view(['GET'])
def FavoriteByPhysiotheripst(request,physio_id):
    try:
        physio = Physiotherapist.objects.get(pk=physio_id)
        print(physio)
    except Physiotherapist.DoesNotExist:
        return Response({'message': 'The Physiotherapist does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            favorite=physio.Physio_Fav.all()
            i=0
            list = []
            for f in favorite:

                pat=Patient.objects.get(pk=favorite[i].Patient_Favorite.pk)
                list.append(pat)
                i=i+1

        except Favorite.DoesNotExist:
            return Response({'message': 'No Favorites'}, status=status.HTTP_404_NOT_FOUND)

        patient = PatientSerializer(list, many=True)
        return Response(patient.data)
class FavoriteList(APIView):
    def get(self,request):
        favorites = Favorite.objects.all()
        data=FavoriteSerializer(favorites,many=True).data
        return Response(data)
    def post(self,request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)