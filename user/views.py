from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes

from user.serializers import *
from services.functions import send_activation_email
from services.response import *
from services.utility import *
from .models import *
from rest_framework import status

User = get_user_model()
generate_token = EmaiLVerIficationTokenGenerator()


@permission_classes((AllowAny,))
class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return bad_request_response(serializer.errors)
        check_user = User.objects.all().filter(username=request.data['email'])
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
        if token:
            return create_response({'token': token.key})
        return bad_request_response({'Message': "Invalid Username or Password!"})


@permission_classes((IsAuthenticated,))
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    def update(self, request, *args, **kwargs):
        self.object = self.request.user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return create_response({"message": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return create_response({"message": 'success'} , status = status.HTTP_200_OK)
        return create_response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny,))
class ResetPasswordView(generics.CreateAPIView):
    serializer_class = resetPasswordSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return bad_request_response({"message": "email not valid"} , status = status.HTTP_400_BAD_REQUEST)
        obj = User.objects.filter(email=request.data["email"])
        if obj:
            #TODO : alankar write that email verification function

            return create_response({"mesage": 'email sent'} , status = status.HTTP_200_OK)
        return bad_request_response({'Message': "Email not sent account not exsist"} , status = status.HTTP_400_BAD_REQUEST)


def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id = uid)
    except Exception as e:
        user = None
    
    if user and generate_token.check_token(user, token):
        User.objects.filter(id=uid).update(is_active = True)
        return redirect(reverse("login"))
    return JsonResponse({'Message': "Account activation failed"})

