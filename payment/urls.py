from django.urls import path

from .views import *

urlpatterns = [
    path("billing", GetBillingUserData.as_view(), name="billing"),
    path("success-payment", success_payment, name="success-payment"),
]