from rest_framework import serializers

from TaiyoInfo.models import Category, GeneralInfo, Addres, NewsLetter , Policy, Product , Subscription , Contact
from services.serializers import ForeignKeyField


class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = "__all__"

class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = "__all__"
        read_only_fields = ['generation_time']

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = "__all__"

class AddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addres
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = ForeignKeyField(queryset=Category.objects, filter_by="name")
    class Meta:
        model = Product
        fields = "__all__"




class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"



class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"