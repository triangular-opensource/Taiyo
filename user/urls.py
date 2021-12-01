from django.urls import path

from user.views import ChangePasswordView, LoginAPIView, RegisterAPI, ResetPasswordView

urlpatterns = [
    path('register', RegisterAPI.as_view(), name="register"),
    path('login', LoginAPIView.as_view(), name="login"),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),
    path('reset-password', ResetPasswordView.as_view(), name='reset-password'),
]