from django.urls import path

from .views import *

urlpatterns = [
    path("billing", GetBillingUserData.as_view(), name="billing"),
    path("success-payment", SuccessPayment.as_view(), name="success-payment"),
]