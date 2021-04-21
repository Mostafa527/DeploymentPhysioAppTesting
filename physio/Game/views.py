from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from physio.models import *
from physio.serializer import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view


class GametList(APIView):
    def get(self,request):
        games = Game.objects.all()
        data=GameSerializer(games,many=True).data
        return Response(data)
