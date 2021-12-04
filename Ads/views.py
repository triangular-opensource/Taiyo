from rest_framework import generics
from rest_framework.views import APIView

from Ads.serializers import AdImagesSerializer ,   AdvertismentSerializer , BidSerializer
from services.mailing import sendNewsEmail

from services.response import success_response, bad_request_response, empty_response, create_response, not_found_response


from Ads.models import Advertisement  , Bid ,  AdImages



class AdvertismentView(generics.RetrieveAPIView):
    serializer_class = AdvertismentSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Advertisement.objects.all(), many=True)
        return success_response(serializer.data)



class BidView(generics.RetrieveAPIView):
    serializer_class = BidSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Bid.objects.all(), many=True)
        return success_response(serializer.data)


class AdImagesView(generics.RetrieveAPIView):
    serializer_class = AdImagesSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(AdImages.objects.all(), many=True)
        return success_response(serializer.data)






