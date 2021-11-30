from django.shortcuts import get_object_or_404, redirect, render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes

from users.serializers import *
from services.response import *
from services.utility import *
from .models import *

User = get_user_model()
generate_token = EmaiLVerIficationTokenGenerator()


@permission_classes((AllowAny,))
class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return bad_request_response(serializer.errors)
        check_user = User.objects.all().filter(email=request.data['email'], username=request.data['username'])
        if not check_user:
            user = User.objects.create_user(first_name=request.data['first_name'], last_name=request.data['last_name'],
                                            username=request.data['username'], email=request.data['email'],
                                            password=request.data['password'], is_active=False)
            user.save()
            send_activation_email(user, request)
            return create_response({"message": "Email Activation Link Sent."})
        else:
            return bad_request_response({"message": "user with this username exsist"})


@permission_classes((AllowAny,))
class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return bad_request_response(serializer.errors)
        if request.data["email"] is not None or request.data['email'] != "":
            user = get_object_or_404(User, email=request.data["email"])
            token = create_token(username=user.username, password=request.data['password'])
        elif request.data["username"] is not None or request.data['username'] != "":
            token = create_token(username=request.data["username"], password=request.data['password'])
        if token:
            return create_response({'token': token.key})
        return bad_request_response({'Message': "Invalid Username or Password!"})





