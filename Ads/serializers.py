from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from Ads.models import *


class AdvertisementViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id',
                  'image_1_link',
                  'product_description',
                  'timestamp',
                  'author_business_address',
                  'author_country',
                  'buy_or_sell',
                  'bidding_close_date',
                  'basic_price']

class AdvertisementSerializer(serializers.ModelSerializer):
    image_1 = serializers.FileField(required=False)
    class Meta:
        model = Advertisement
        fields = "__all__"
        read_only_field = "image_1"


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"
