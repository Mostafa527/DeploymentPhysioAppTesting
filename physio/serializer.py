from rest_framework import serializers
from .models import *


class ClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields= "__all__"

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields ="__all__"


class PhysiotherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physiotherapist
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

class Exercise_Plan_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise_Plan
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Session
        fields = "__all__"
class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Observations
        fields = "__all__"