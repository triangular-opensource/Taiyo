from rest_framework import generics
from Ads.serializers import AdImagesSerializer ,   AdvertismentSerializer , BidSerializer
from services.response import success_response, bad_request_response, empty_response
from Ads.models import Advertisement  , Bid ,  AdImages



class AdvertismentView(generics.RetrieveAPIView):
    serializer_class = AdvertismentSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Advertisement.objects.all(), many=True)
        return success_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)


class AdvertismentChanges(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class =  AdvertismentSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Advertisement.objects.get(id=kwargs['id']))
        return success_response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = generics.get_object_or_404( AdvertismentSerializer, id=kwargs['id'])
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(  AdvertismentSerializer , id=kwargs['id'])
        instance.delete()
        return empty_response()



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


class BidChanges(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class =  BidSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Bid.objects.get(id=kwargs['id']))
        return success_response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = generics.get_object_or_404( BidSerializer, id=kwargs['id'])
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(  BidSerializer , id=kwargs['id'])
        instance.delete()
        return empty_response()

class AdImagesView(generics.RetrieveAPIView):
    serializer_class = AdImagesSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(AdImages.objects.all(), many=True)
        return success_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)


class AdImagesChanges(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class =  AdImagesSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer( AdImages.objects.get(id=kwargs['id']))
        return success_response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = generics.get_object_or_404( AdImagesSerializer, id=kwargs['id'])
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(  AdImagesSerializer , id=kwargs['id'])
        instance.delete()
        return empty_response()




