from rest_framework import generics
from TaiyoInfo.serializers import GeneralInfoSerializer , PolicySerializer , AddresSerializer , NewsLetterSerializer
from services.mailing import sendNewsEmail

from services.response import success_response, bad_request_response, empty_response, create_response, not_found_response

from TaiyoInfo.models import GeneralInfo, NewsLetter, Addres , Policy


class GeneralInfoView(generics.RetrieveAPIView):
    serializer_class = GeneralInfoSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(GeneralInfo.objects.all(), many=True)
        return success_response(serializer.data)


class PolicyView(generics.RetrieveAPIView):
    serializer_class = PolicySerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Policy.objects.all(), many=True)
        return success_response(serializer.data)

class AddressView(generics.RetrieveAPIView):
    serializer_class = GeneralInfoSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Addres.objects.all(), many=True)
        return success_response(serializer.data)


class NewsLetterView(generics.RetrieveAPIView):
    serializer_class = GeneralInfoSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(NewsLetter.objects.all(), many=True)
        return success_response(serializer.data)









