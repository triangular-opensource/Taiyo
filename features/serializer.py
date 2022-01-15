from rest_framework import serializers
from features.models import *
from services.serializers import ForeignKeyField

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = ForeignKeyField(queryset=Category.objects, filter_by="name")
    class Meta:
        model = Product
        fields = "__all__"




class ProductFieldSerializer(serializers.ModelSerializer):
    product = ForeignKeyField(queryset=Product.objects, filter_by="name")
    class Meta:
        model = ProductFields
        fields = "__all__"

