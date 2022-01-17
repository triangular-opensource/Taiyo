from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from Ads.models import *
from services.serializers import ForeignKeyField


class AdvertisementViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id',
                  'image_1_link',
                  'product_description',
                  'timestamp',
                  'location',
                  'buy_or_sell',
                  'bidding_close_date',
                  'basic_price',
                  'latitude',
                  'longitude'
                  ]

class AdvertisementSerializer(serializers.ModelSerializer):
    image_1 = serializers.FileField(required=False)
    product = ForeignKeyField(queryset=Product.objects, filter_by="name")
    selected_bid_amount = serializers.CharField(source="selected_bid.amount", allow_null=True, allow_blank=True, required=False)
    user__first_name = serializers.CharField(source="selected_bid.user.first_name", allow_null=True, allow_blank=True, required=False)
    user__middle_name = serializers.CharField(source="selected_bid.user.middle_name", allow_null=True, allow_blank=True, required=False)
    user__last_name = serializers.CharField(source="selected_bid.user.last_name", allow_null=True, allow_blank=True, required=False)
    user__email = serializers.CharField(source="selected_bid.user.email", allow_null=True, allow_blank=True, required=False)
    user__phone_number = serializers.CharField(source="selected_bid.user.phone_number", allow_null=True, allow_blank=True, required=False)
    email = serializers.CharField(source="user.email", allow_null=True, allow_blank=True, required=False)
    class Meta:
        model = Advertisement
        fields = [
            "id",
            "product",
            "buy_or_sell",
            "excel_file_link",
            "pdf_file_link",
            "image_1",
            "image_1_link",
            "image_2_link",
            "image_3_link",
            "image_4_link",
            "quality",
            "dimensions",
            "grade",
            "temper",
            "specification_number",
            "quantity",
            "coating_in_gsm",
            "product_description",
            "bidding",
            "bidding_close_date",
            "selected_bid",
            "selected_bid_amount", 
            "name",
            "mobile_number",
            "email",
            "location",
            "business_address",
            "color",
            "user",
            "timestamp",
            "user__first_name",
            "user__middle_name",
            "user__last_name",
            "user__email",
            "user__phone_number",
            "basic_price",
            "approval",
            "visible",
            "latitude",
            "longitude"
        ]
        read_only_field = [
            "image_1",
            "selected_bid_amount", 
            "user__first_name",
            "user__middle_name",
            "user__last_name",
            "user__email",
            "user__phone_number",
        ]


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"
