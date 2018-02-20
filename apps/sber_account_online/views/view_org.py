from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from apps.sber_account_online.models.model_org import Organization
from apps.sber_account_online.serializers.serializer_org import OrganizationSerializer


class OrganizationListView(generics.ListAPIView):
    """
    Возвращаем список разрешенных атрубутов для поиска
    """
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()