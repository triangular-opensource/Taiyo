from django.urls import path

from user.views import *

urlpatterns = [
    path('user', UserView.as_view(), name="user"),
    path('user/<int:id>', UserChanges.as_view(), name="user edit view"),
    path('register', RegisterAPI.as_view(), name="register"),
    path('login', LoginAPIView.as_view(), name="login"),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),
    path('reset-password', ResetPasswordTokenView.as_view(), name='reset-password'),
    path('reset-password-token/<str:email>', RPTChangeView.as_view(), name='reset-password-token'),
]