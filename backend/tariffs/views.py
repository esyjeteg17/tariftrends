from django.contrib.auth import authenticate
from django.shortcuts import render
from django_filters import rest_framework as filters, NumberFilter, BaseInFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Tariff, ModemTariff, HomephoneTariff, TVTariff, InternetTariff, SmartTariff
from .serializers import TariffsSerializer, ModemTariffSerializer, HomephoneTariffSerializer, TVTariffSerializer, \
    InternetTariffSerializer, SmartTariffSerializer, RegisterSerializer, UpdateFavoriteSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status


class PriceOperatorFilter(filters.FilterSet):
    price_from = NumberFilter(field_name="price", lookup_expr='gte')
    price_to = NumberFilter(field_name="price", lookup_expr='lte')
    operator = BaseInFilter(method='filter_operators')

    class Meta:
        model = Tariff
        fields = []

    def filter_operators(self, queryset, name, value):
        valid_operators = [v for v in value if v not in (None, 'undefined', '')]
        if valid_operators:
            return queryset.filter(**{f"{name}__in": valid_operators})
        else:
            return queryset


class PriceOperatorFilterModem(filters.FilterSet):
    price_from = NumberFilter(field_name="price", lookup_expr='gte')
    price_to = NumberFilter(field_name="price", lookup_expr='lte')
    operator = BaseInFilter(method='filter_operators')

    class Meta:
        model = ModemTariff
        fields = []

    def filter_operators(self, queryset, name, value):
        valid_operators = [v for v in value if v not in (None, 'undefined', '')]
        if valid_operators:
            return queryset.filter(**{f"{name}__in": valid_operators})
        else:
            return queryset


class PriceOperatorFilterHomephone(filters.FilterSet):
    price_from = NumberFilter(field_name="price", lookup_expr='gte')
    price_to = NumberFilter(field_name="price", lookup_expr='lte')
    operator = BaseInFilter(method='filter_operators')

    class Meta:
        model = HomephoneTariff
        fields = []

    def filter_operators(self, queryset, name, value):
        valid_operators = [v for v in value if v not in (None, 'undefined', '')]
        if valid_operators:
            return queryset.filter(**{f"{name}__in": valid_operators})
        else:
            return queryset


class PriceOperatorFilterTV(filters.FilterSet):
    price_from = NumberFilter(field_name="price", lookup_expr='gte')
    price_to = NumberFilter(field_name="price", lookup_expr='lte')
    operator = BaseInFilter(method='filter_operators')

    class Meta:
        model = TVTariff
        fields = []

    def filter_operators(self, queryset, name, value):
        valid_operators = [v for v in value if v not in (None, 'undefined', '')]
        if valid_operators:
            return queryset.filter(**{f"{name}__in": valid_operators})
        else:
            return queryset


class PriceOperatorFilterInternet(filters.FilterSet):
    price_from = NumberFilter(field_name="price", lookup_expr='gte')
    price_to = NumberFilter(field_name="price", lookup_expr='lte')
    operator = BaseInFilter(method='filter_operators')

    class Meta:
        model = InternetTariff
        fields = []

    def filter_operators(self, queryset, name, value):
        valid_operators = [v for v in value if v not in (None, 'undefined', '')]
        if valid_operators:
            return queryset.filter(**{f"{name}__in": valid_operators})
        else:
            return queryset


class PriceOperatorFilterSmart(filters.FilterSet):
    price_from = NumberFilter(field_name="price", lookup_expr='gte')
    price_to = NumberFilter(field_name="price", lookup_expr='lte')
    operator = BaseInFilter(method='filter_operators')

    class Meta:
        model = SmartTariff
        fields = []

    def filter_operators(self, queryset, name, value):
        valid_operators = [v for v in value if v not in (None, 'undefined', '')]
        if valid_operators:
            return queryset.filter(**{f"{name}__in": valid_operators})
        else:
            return queryset


class TariffsAPIView(generics.ListAPIView):
    queryset = Tariff.objects.all()
    serializer_class = TariffsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PriceOperatorFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('name')
        sort_by = self.request.query_params.get('sortBy')

        if search_term:
            queryset = queryset.filter(name__icontains=search_term.strip('*'))

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset


class UpdateFavoriteAPIView(generics.UpdateAPIView):
    queryset = Tariff.objects.all()
    serializer_class = UpdateFavoriteSerializer


class ModemTariffAPIView(generics.ListAPIView):
    queryset = ModemTariff.objects.all()
    serializer_class = ModemTariffSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PriceOperatorFilterModem

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('name')
        sort_by = self.request.query_params.get('sortBy')

        if search_term:
            queryset = queryset.filter(name__icontains=search_term.strip('*'))

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset



class HomephoneTariffAPIView(generics.ListAPIView):
    queryset = HomephoneTariff.objects.all()
    serializer_class = HomephoneTariffSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PriceOperatorFilterHomephone

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('name')
        sort_by = self.request.query_params.get('sortBy')

        if search_term:
            queryset = queryset.filter(name__icontains=search_term.strip('*'))

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset


class TVTariffAPIView(generics.ListAPIView):
    queryset = TVTariff.objects.all()
    serializer_class = TVTariffSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PriceOperatorFilterTV

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('name')
        sort_by = self.request.query_params.get('sortBy')

        if search_term:
            queryset = queryset.filter(name__icontains=search_term.strip('*'))

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset


class InternetTariffAPIView(generics.ListAPIView):
    queryset = InternetTariff.objects.all()
    serializer_class = InternetTariffSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PriceOperatorFilterInternet

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('name')
        sort_by = self.request.query_params.get('sortBy')

        if search_term:
            queryset = queryset.filter(name__icontains=search_term.strip('*'))

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset


class SmartTariffAPIView(generics.ListAPIView):
    queryset = SmartTariff.objects.all()
    serializer_class = SmartTariffSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PriceOperatorFilterSmart

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('name')
        sort_by = self.request.query_params.get('sortBy')

        if search_term:
            queryset = queryset.filter(name__icontains=search_term.strip('*'))

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

