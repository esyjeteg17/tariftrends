from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Tariff, ModemTariff, HomephoneTariff, TVTariff, InternetTariff, SmartTariff
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response


class TariffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class UpdateFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ['isFavotite']


    def update(self, instance, validated_data):
        instance.isFavotite = validated_data.get('isFavotite', instance.isFavotite)
        instance.save()
        return instance


class ModemTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModemTariff
        fields = '__all__'


class HomephoneTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomephoneTariff
        fields = '__all__'


class TVTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVTariff
        fields = '__all__'



class InternetTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternetTariff
        fields = '__all__'



class SmartTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartTariff
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], username=validated_data['username'], password=validated_data['password'])
        return user



