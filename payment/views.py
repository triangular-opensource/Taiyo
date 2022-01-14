import json
from django.conf import settings
from django.shortcuts import redirect

from rest_framework.permissions import IsAuthenticated
import razorpay
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from services.response import bad_request_response, success_response
from razorpay import client

from .models import Payment
from TaiyoInfo.models import Subscription

from datetime import timedelta

from django.core.mail import send_mail, mail_managers

User = get_user_model()

RAZORPAY_KEY_ID = "rzp_test_240llZpXCqHDn1"
RAZORPAY_KEY_SECRET = "T0q35yVD5dQERgOVDJvVDKzJ"

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))


@permission_classes((IsAuthenticated, ))
class GetBillingUserData(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        amount = int(data.get("amount"))
        subscription = Subscription.objects.filter(id=int(data.get("package"))).first()
        order = client.order.create({"amount":amount*100, "currency":"INR"})
        order = Payment(user=request.user, amount=amount, order_id=order['id'], package=subscription)
        order.save()
        return success_response({"data": model_to_dict(order)})


@csrf_exempt
def success_payment(request):    
    if request.method == "POST":
        data = request.POST
        order_id = Payment.objects.filter(order_id=data['razorpay_order_id']).last().order_id
        parameters = {
            "razorpay_order_id": order_id,
            "razorpay_payment_id": data['razorpay_payment_id'],
            "razorpay_signature": data['razorpay_signature']
        }
        signature = client.utility.verify_payment_signature(parameters=parameters)
        
        if signature is None:
            order = Payment.objects.filter(order_id=data['razorpay_order_id'])
            order.update(payment_id=data['razorpay_payment_id'], payment_signature=data['razorpay_signature'], paid=True)
            try:
                send_mail(
                    f"Payment Successfully Completed for Rs. {order[0].amount} on Taiyo",
                    f"Thank you for subscribing at Taiyo.\n\nFor confirmation or proof you can contact us at taiyo.apex@gmail.com\n\nWe hope you are enjoying our services\n\nThank You\nRegards Taiyo",
                    "taiyo.apex@gmail.com",
                    [order.user.email],
                    fail_silently=False
                )
                mail_managers(
                    f"Payment Recieved of Rs. {order[0].amount} from {order.user.name}",
                    f"Please Confirm the payment of Rs. {order[0].amount}.\n\nThank You\nRegards Taiyo",
                    fail_silently=False
                )
            except Exception as e:
                pass
            
            # TODO: GST Calculation Stuff

            # total_balance = order.user.total_balance
            # curr_balance = order.user.balance
            # gst = order[0].amount*18/(100 + 18)
            # amount_without_gst = order[0].amount - gst
            # total_balance += amount_without_gst
            # curr_balance += amount_without_gst

            subscription = Subscription.objects.get(amount=int(order[0].amount))
            User.objects.filter(email=order[0].user.email, id=order[0].user.id).update(
                package_type = subscription,
                package_expiry = order[0].user.package_expiry + timedelta(days=int(subscription.days))
            )
            
            return redirect(f"{settings.FRONTEND_URL}/package-history?payment=success")
        else:
            return redirect(f"{settings.FRONTEND_URL}/package-history")
