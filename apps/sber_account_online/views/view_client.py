from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from apps.sber_account_online.models.model_client import Client
from apps.sber_account_online.serializers.serializer_client import SberClientSerializer


class ClientListView(generics.ListAPIView):
    """
    Возвращаем список разрешенных атрубутов для поиска
    """
    serializer_class = SberClientSerializer
    queryset = Client.objects.all()