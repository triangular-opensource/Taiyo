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
                  'author_business_address',
                  'author_country',
                  'buy_or_sell',
                  'bidding_close_date',
                  'basic_price']

class AdvertisementSerializer(serializers.ModelSerializer):
    image_1 = serializers.FileField(required=False)
    product = ForeignKeyField(queryset=Product.objects, filter_by="name")
    selected_bid = ForeignKeyField(queryset=Bid.objects, filter_by="amount")
    selected_bid_amount = serializers.CharField(source="selected_bid.amount")
    user__first_name = serializers.CharField(source="selected_bid.user.first_name")
    user__middle_name = serializers.CharField(source="selected_bid.user.middle_name")
    user__last_name = serializers.CharField(source="selected_bid.user.last_name")
    user__email = serializers.CharField(source="selected_bid.user.email")
    user__phone_number = serializers.CharField(source="selected_bid.user.phone_number")
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
            "thickness",
            "width",
            "length",
            "grade_or_spec",
            "temper",
            "specification_number",
            "quantity",
            "coating_in_gsm",
            "product_description",
            "bidding",
            "bidding_close_date",
            "selected_bid",
            "selected_bid_amount", 
            "author_name",
            "author_mobile_number",
            "author_country",
            "author_business_address",
            "user",
            "timestamp",
            "user__first_name",
            "user__middle_name",
            "user__last_name",
            "user__email",
            "user__phone_number",
        ]
        read_only_field = [
            "image_1",
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
