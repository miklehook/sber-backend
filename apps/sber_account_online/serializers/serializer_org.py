
from rest_framework import serializers

from apps.sber_account_online.models.model_org import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('FIO',)