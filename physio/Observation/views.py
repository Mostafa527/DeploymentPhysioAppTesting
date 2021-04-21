
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from physio.models import *
from physio.serializer import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(['GET', 'PUT'])
def observation_detail(request, observation_id):
    try:
        observation =Observations.objects.get(pk=observation_id)
    except Observations.DoesNotExist:
        return Response({'message': 'No Observations'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        observation_serializer = ObservationSerializer(observation)
        return Response(observation_serializer.data)

    elif request.method == 'PUT':
        observation_data = JSONParser().parse(request)
        observation_serializer = ObservationSerializer(observation, data=observation_data)
        if observation_serializer.is_valid():
            observation_serializer.save()
            return Response(observation_serializer.data)
        return Response(observation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObservationList(APIView):
    def get(self,request):
        observations = Observations.objects.all()
        data=ObservationSerializer(observations,many=True).data
        return Response(data)
    def post(self,request):
        serializer = ObservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ObservationDetailsBySession(request,session_id):
    try:
        session = Session.objects.get(pk=session_id)
    except Session.DoesNotExist:
        return Response({'message': 'The Session does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            observation=session.session_observ.all()
        except Observations.DoesNotExist:
            return Response({'message': 'No Observations is existed'}, status=status.HTTP_404_NOT_FOUND)
        observation_serializer = ObservationSerializer(observation,many=True)
        return Response(observation_serializer.data)
