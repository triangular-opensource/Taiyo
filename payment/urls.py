from django.urls import path

from .views import *

urlpatterns = [
    path("recharge/", recharge, name="recharge"),
    path("billing/", billing, name="billing"),
    path("success-payment/", success_payment, name="success-payment"),
]