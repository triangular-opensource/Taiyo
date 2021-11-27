from rest_framework.serializers import ModelSerializer

from TaiyoInfo.models import GeneralInfo


class GeneralInfoSerializer(ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = "__all__"