from rest_framework import serializers

from Ads.models import *


class AdvertisementViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id',
                  'image_1_link',
                  'description',
                  'timestamp',
                  'author_business_address',
                  'author_country']

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"
