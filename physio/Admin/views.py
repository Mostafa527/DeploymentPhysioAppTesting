
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
def admin_detail(request, admin_id):
    try:
        admin =Admin.objects.get(pk=admin_id)
    except Admin.DoesNotExist:
        return Response({'message': 'The Admin does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        admin_serializer = AdminSerializer(admin)
        return Response(admin_serializer.data)

    elif request.method == 'PUT':
        admin_data = JSONParser().parse(request)
        admin_serializer = AdminSerializer(admin, data=admin_data)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return Response(admin_serializer.data)
        return Response(admin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        admin.delete()
        return Response({'message': 'Admin was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class adminList(APIView):
    def get(self,request):
        admins = Admin.objects.all()
        data=AdminSerializer(admins,many=True).data
        return Response(data)
    def post(self,request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)