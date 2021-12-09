import math
import random

from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from services.mailing import send_email

from user.serializers import *
from services.functions import send_activation_email
from services.response import *
from services.utility import *
from .models import *
from django.contrib.auth import get_user_model

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
            user = User.objects.create_user(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                middle_name=request.data['middle_name'],
                username=request.data['email'],
                email=request.data['email'],
                password=request.data['password'],
                is_active=False,
                image=request.data['image'],
                gst_number=request.data['gst_number'],
                phone_number=request.data['phone_number'],
                company_name=request.data['company_name'],
                company_type=request.data['company_type'],
                company_address=request.data['company_address'],
                company_city=request.data['company_city'],
                company_state=request.data['company_state'],
                company_country=request.data['company_country'],
                company_pin_code=request.data['company_pin_code'],
            )
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
            elif not user.is_active:
                return bad_request_response({"message": "Your email isn't verified! Please verify than try to login."})
            else:
                return bad_request_response({"message": "Invalid Username/Password"})


@permission_classes((IsAuthenticated,))
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    def update(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return bad_request_response({"message": ["Wrong password."]})
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return create_response({"message": 'success'})
        return bad_request_response(serializer.errors)

@permission_classes((AllowAny,))
class ResetPasswordTokenView(generics.CreateAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return bad_request_response(serializer.errors)
        obj = User.objects.filter(username=request.data["email"])
        if obj:
            digits = [i for i in range(0, 10)]
            token = ""
            for _ in range(6):
                index = math.floor(random.random() * 10)
                token += str(digits[index])
            if token:
                send_email(
                        subject="Your Reset Token of Taiyo",
                        message=token,
                        to=request.data['email']
                )
                Token.objects.create(token=token, email=request.data["email"])
                return create_response({'message': 'email sent'})
            return bad_request_response({'Message': "Invalid Username or Password!"})
        else:
            return bad_request_response({'Message': "Email not sent 2"})


@permission_classes((AllowAny,))
class RPTChangeView(generics.CreateAPIView):
    serializer_class = ResetPasswordTokenSerializer

    def post(self, request, email, *args, **kwargs):
        obj = Token.objects.filter(email=email).last()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if obj.token == request.data["token"]:
                user = User.objects.get(email=email)
                user.set_password(request.data["password"])
                user.save()
                Token.objects.filter(email=email).delete()
                return create_response({'status': 'success'})
            return bad_request_response(serializer.errors)
        return bad_request_response({'Message': "failure"})


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


@permission_classes((IsAuthenticated, ))
class UserProfileView(generics.RetrieveAPIView, generics.UpdateAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return success_response(serializer.data)

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)


@permission_classes((AllowAny ,))
class UserChanges(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(User.objects.get(id=kwargs['id']))
        return success_response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = generics.get_object_or_404( UserSerializer, id=kwargs['id'])
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(  UserSerializer , id=kwargs['id'])
        instance.delete()
        return empty_response()




