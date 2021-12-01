from rest_framework import serializers
import re



class RegisterSerializer(serializers.Serializer):

    first_name = serializers.CharField(required=True, max_length=75)
    middle_name = serializers.charField(max_length=True)
    last_name = serializers.CharField(max_length=75)
    username = serializers.CharField(required=True, max_length=75)
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
                  'username',
                  'email',
                  'password',
                  'gst_number',
                  'phone_number',
                  'company_name',
                  'company_address',
                  'company_city',
                  'company_state','company_country',
                  'company_pin_code'
                  ]

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

class resetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


