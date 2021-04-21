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
def exerciseplan_detail(request, exerciseplan_id):
    try:
        exercise_plan =Exercise_Plan.objects.get(pk=exerciseplan_id)
    except Exercise_Plan.DoesNotExist:
        return Response({'message': 'No Exercise Plan'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        exerciseplan_serializer = Exercise_Plan_Serializer(exercise_plan)
        return Response(exerciseplan_serializer.data)

    elif request.method == 'PUT':
        exerciseplan_data = JSONParser().parse(request)
        exerciseplan_serializer = Exercise_Plan_Serializer(exercise_plan, data=exerciseplan_data)
        if exerciseplan_serializer.is_valid():
            exerciseplan_serializer.save()
            return Response(exerciseplan_serializer.data)
        return Response(exerciseplan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        exercise_plan.delete()
        return Response({'message': 'ExercisePlan was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class ExercisePlanList(APIView):
    def get(self,request):
        exercise_plans = Exercise_Plan.objects.all()
        data=Exercise_Plan_Serializer(exercise_plans,many=True).data
        return Response(data)
    def post(self,request):
        serializer =Exercise_Plan_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ExercisePlanDetailsByPatient(request,patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Physiotherapist.DoesNotExist:
        return Response({'message': 'The Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            exercise_plan=patient.Patient_Plan.all()
        except Exercise_Plan.DoesNotExist:
            return Response({'message': 'No ExercisePlan Existed'}, status=status.HTTP_404_NOT_FOUND)
        exerciseplan_serializer = Exercise_Plan_Serializer(exercise_plan,many=True)
        return Response(exerciseplan_serializer.data)


@api_view(['GET'])
def ValidExercisePlanByPatient(request,physio_id):
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


