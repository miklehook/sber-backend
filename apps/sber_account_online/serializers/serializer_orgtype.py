
from rest_framework import serializers

from apps.sber_account_online.models.model_orgtype import OrgType


class OrgTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgType
        fields = ('short_name','full_name',)