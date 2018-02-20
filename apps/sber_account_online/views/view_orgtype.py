from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from apps.sber_account_online.models.model_orgtype import OrgType
from apps.sber_account_online.serializers.serializer_orgtype import OrgTypeSerializer


class OrgTypeListView(generics.ListAPIView):
    """
    Возвращаем список разрешенных атрубутов для поиска
    """
    serializer_class = OrgTypeSerializer
    queryset = OrgType.objects.all()