
from rest_framework import serializers

from apps.sber_account_online.models.model_client import Client


class SberClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('FIO',)