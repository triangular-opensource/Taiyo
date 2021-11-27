from rest_framework import serializers

from TaiyoInfo.models import GeneralInfo


class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = "__all__"