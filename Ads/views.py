from rest_framework import generics
from Ads.serializers import AdvertisementSerializer, BidSerializer , AdvertisementViewSerializer
from services.response import success_response, bad_request_response, empty_response
from Ads.models import Advertisement, Bid
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes


@permission_classes((AllowAny,))
class AdvertismentView(generics.RetrieveAPIView):
    serializer_class = AdvertisementViewSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Advertisement.objects.all().order_by("-timestamp"), many=True)
        return success_response(serializer.data)


@permission_classes((IsAuthenticated,))
class AdvertisementPostView(generics.RetrieveAPIView):
    serializer_class = AdvertisementSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)


@permission_classes((IsAuthenticated,))
class AdvertismentChanges(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = AdvertisementSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Advertisement.objects.get(id=kwargs['id']))
        return success_response(serializer.data)

    def put(self, request, *args, **kwargs):
        try:
            instance = Advertisement.objects.get(id=kwargs['id'])
            serializer = self.get_serializer(instance=instance, data=request.data)
        except Exception:
            return bad_request_response({"message": "ad not exist"})
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(AdvertisementSerializer , id=kwargs['id'])
        instance.delete()
        return empty_response()


@permission_classes((IsAuthenticated,))
class BidView(generics.RetrieveAPIView):

    serializer_class = BidSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Bid.objects.all(), many=True)
        return success_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)

@permission_classes((IsAuthenticated,))
class BidChanges(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = BidSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Bid.objects.filter( advertisement =kwargs['id']) , many = True)
        return success_response(serializer.data)

    def put(self, request, *args, **kwargs):
        try:
            bid = Bid.objects.get(id=kwargs['id'])
            serializer = self.get_serializer(bid, data=request.data)
        except Exception:
            return bad_request_response({"message": "bid not exist"})
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(  BidSerializer ,   advertisement =kwargs['id'])
        instance.delete()
        return empty_response()
