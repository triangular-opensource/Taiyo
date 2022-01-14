from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from TaiyoInfo.serializers import GeneralInfoSerializer, PolicySerializer, AddresSerializer, NewsLetterSerializer, SubscriptionSerializer , ContactSerializer
from services.functions import sendNewsEmail

from services.response import success_response, bad_request_response
from services.mailing import *


from TaiyoInfo.models import GeneralInfo, NewsLetter, Addres , Policy, Subscription , Contact



@permission_classes((AllowAny, ))
class GeneralInfoView(generics.RetrieveAPIView):
    serializer_class = GeneralInfoSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(GeneralInfo.objects.all(), many=True)
        return success_response(serializer.data)


@permission_classes((AllowAny, ))
class PolicyView(generics.RetrieveAPIView):
    serializer_class = PolicySerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Policy.objects.all(), many=True)
        return success_response(serializer.data)


@permission_classes((AllowAny, ))
class AddressView(generics.RetrieveAPIView):
    serializer_class = AddresSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Addres.objects.all(), many=True)
        return success_response(serializer.data)


@permission_classes((AllowAny, ))
class NewsLetterView(generics.RetrieveAPIView, generics.CreateAPIView):
    serializer_class = NewsLetterSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(NewsLetter.objects.all(), many=True)
        return success_response(serializer.data)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sendNewsEmail(request.data['email'])
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)




@permission_classes((AllowAny,))
class ContactView(generics.RetrieveAPIView, generics.CreateAPIView):
    serializer_class = ContactSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Contact.objects.all(), many=True)
        return success_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "name": request.data["name"],
                "email" : request.data["email"],
                "subject" : request.data["subject"],
                "message" : request.data["message"]
            }
            sendContactEmail(data)
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)

def admin_redirect(request):
    return redirect("admin/")






@permission_classes((AllowAny, ))
class SubscriptionView(generics.RetrieveAPIView):
    serializer_class = SubscriptionSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Subscription.objects.all(), many=True)
        return success_response(serializer.data)



