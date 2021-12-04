from rest_framework import serializers

from Ads.models import *

class AdvertismentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"

class AdImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdImages
        fields = "__all__"


