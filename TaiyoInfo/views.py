from rest_framework import generics
from rest_framework.decorators import permission_classes
from TaiyoInfo.serializers import GeneralInfoSerializer

from services.response import success_response, bad_request_response, empty_response, create_response, not_found_response

from TaiyoInfo.models import GenralInfo


class OrganizationView(generics.RetrieveAPIView):
    serializer_class = GeneralInfoSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(GenralInfo.objects.all())
        return success_response(serializer.data)
