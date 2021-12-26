from rest_framework import serializers
import re
from django.contrib.auth import get_user_model

User = get_user_model()
from user.models import Notification

class RegisterSerializer(serializers.Serializer):

    first_name = serializers.CharField(required=True, max_length=75)
    middle_name = serializers.CharField(required=False, max_length=30)
    last_name = serializers.CharField(required=True, max_length=75)
    gst_number = serializers.CharField(required= True,max_length=16)
    phone_number = serializers.CharField(required=True, max_length=16)

    company_name = serializers.CharField(required=True, max_length=50)
    company_type = serializers.CharField(required=True , max_length=30)
    company_address = serializers.CharField(required=True , max_length=50)
    company_city = serializers.CharField(required=True , max_length=50)
    company_state = serializers.CharField(required=True , max_length=50)
    company_country = serializers.CharField(required=True , max_length=50)
    company_pin_code = serializers.CharField(required=True , max_length=50)

    email = serializers.CharField(required=True, max_length=75)
    password = serializers.CharField(required=True, max_length=50)

    class Meta:
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'password',
            'gst_number',
            'phone_number',
            'company_name',
            'company_address',
            'company_city',
            'company_state',
            'company_country',
            'company_pin_code',
        ]
        optional_fields = ['middle_name',]

    @classmethod
    def validate_email(cls, value):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, value)):
            return False
        return True




class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True, max_length=75)
    password = serializers.CharField(required=True, max_length=50)

    class Meta:
        fields = ['email', 'password']

    @classmethod
    def validate_email(cls, value):
        return value.lower()



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        fields = ['old_password', 'new_password']


class ResetPasswordTokenSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ['token', 'password']

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields = ['email']


class FriendUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "image",
            "phone_number"
        ]

class UserSerializer(serializers.ModelSerializer):
    friends = FriendUserSerializer(many=True)
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "image",
            "gst_number",
            "phone_number",
            "user_type",
            "package_type",
            "package_expiry",
            "company_name",
            "company_type",
            "company_address",
            "company_city",
            "company_state",
            "company_country",
            "company_pin_code",
            "last_login",
            "date_joined",
            "friends"
        ]
        read_only_fields = ["id", "last_login", "date_joined", "email"]




class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id',
                  'heading',
                  'text',
                  'user',
                  'create_time'
                  ]



