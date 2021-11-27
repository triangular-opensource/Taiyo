from rest_framework import generics
from TaiyoInfo.serializers import GeneralInfoSerializer
from services.mailing import sendNewsEmail

from services.response import success_response, bad_request_response, empty_response, create_response, not_found_response

from TaiyoInfo.models import GeneralInfo


class GeneralInfoView(generics.RetrieveAPIView):
    serializer_class = GeneralInfoSerializer

    def get(self, request, *args, **kwargs):
        sendNewsEmail()
        serializer = self.get_serializer(GeneralInfo.objects.all(), many=True)
        return success_response(serializer.data)
