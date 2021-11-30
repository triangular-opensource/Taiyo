from rest_framework import serializers

from TaiyoInfo.models import GeneralInfo


class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = "__all__"

class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = "__all__"

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = "__all__"

class AddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = "__all__"

