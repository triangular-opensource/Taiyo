from rest_framework import serializers

from TaiyoInfo.models import GeneralInfo, Addres, NewsLetter , Policy




class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = "__all__"

class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = "__all__"

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = "__all__"

class AddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addres
        fields = "__all__"

