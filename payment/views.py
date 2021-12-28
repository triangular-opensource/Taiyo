import json

from rest_framework.permissions import IsAuthenticated
import razorpay
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import permission_classes
from services.response import bad_request_response, success_response
from razorpay import client

from .models import Payment
from TaiyoInfo.models import Subscription

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


@permission_classes((IsAuthenticated,))
class SuccessPayment(generics.CreateAPIView):
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = request.data
        order_id = Payment.objects.filter(user=request.user).last().order_id
        parameters = {
            "razorpay_order_id": order_id,
            "razorpay_payment_id": data['razorpay_payment_id'],
            "razorpay_signature": data['razorpay_signature']
        }
        signature = client.utility.verify_payment_signature(parameters=parameters)
        
        if signature is None:
            order = Payment.objects.filter(user=request.user, order_id=data['razorpay_order_id'])
            order.update(payment_id=data['razorpay_payment_id'], payment_signature=data['razorpay_signature'], paid=True)
            try:
                pass
                # send_mail(
                #     f"Payment Successfully Completed for Rs. {order[0].amount} on Tracerz",
                #     f"Thank you for recharging at Tracerz.\n\nFor confirmation or proof you can contact us at admin@tracerz.in\n\nWe hope you are enjoying our services\n\nThank You\nRegards Tracerz",
                #     "noreply@tracerz.in",
                #     [request.user.email],
                #     fail_silently=False
                # )
                # mail_managers(
                #     f"Payment Recieved of Rs. {order[0].amount} from {request.user.name}",
                #     f"Please Confirm the payment and {order[0].amount} to their balance on backend panel.\n\nThank You\nRegards Tracerz",
                #     fail_silently=False
                # )
            except Exception as e:
                pass
            
            # TODO: GST Calculation Stuff

            # total_balance = request.user.total_balance
            # curr_balance = request.user.balance
            # gst = order[0].amount*18/(100 + 18)
            # amount_without_gst = order[0].amount - gst
            # total_balance += amount_without_gst
            # curr_balance += amount_without_gst
            # User.objects.filter(username=request.user.username, id=request.user.id).update(
            #     balance = curr_balance,
            #     total_balance = total_balance,
            #     subscribed = True
            # )
            
            return success_response({"message": "success"})
        else:
            return bad_request_response({"message": "failure"})
