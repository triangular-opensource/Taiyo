from rest_framework import generics
from Ads.serializers import AdvertisementSerializer, BidSerializer , AdvertisementViewSerializer
from services.response import success_response, bad_request_response, empty_response
from Ads.models import Advertisement, Bid
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from django.utils import timezone
from user.models import Notification

@permission_classes((AllowAny,))
class AdvertismentView(generics.RetrieveAPIView):
    serializer_class = AdvertisementViewSerializer
    def get(self, request, *args, **kwargs):
        case = kwargs['id']
        if case == 1: #all active ads
            serializer = self.get_serializer(Advertisement.objects.filter(visible=True, bidding_close_date__gte=timezone.now()).order_by("-id"), many=True)
        elif case == 2: #active adsof user
            serializer = self.get_serializer(Advertisement.objects.filter(bidding_close_date__gte=timezone.now(),visible = True,user=request.user).order_by("-id"), many=True)
        elif case == 3: #inactive ads od user
            serializer = self.get_serializer(Advertisement.objects.filter(bidding_close_date__lte=timezone.now(), user=request.user ).order_by("-id"), many=True)
        elif case == 4:# selected ads of user
            serializer = self.get_serializer(Advertisement.objects.filter(user=request.user).exclude(selected_bid = None ).order_by("-id"),many=True)
        elif case == 5: # add_type buy
            serializer = self.get_serializer(Advertisement.objects.filter(visible=True, bidding_close_date__gte=timezone.now(), buy_or_sell='Buy').order_by("-id"), many=True)
        elif case == 6:# add_type_sell
            serializer = self.get_serializer(Advertisement.objects.filter(visible=True, bidding_close_date__gte=timezone.now(), buy_or_sell='Sell').order_by("-id"), many=True)
        elif case == 7: #category
            serializer = self.get_serializer(Advertisement.objects.filter(visible=True, bidding_close_date__gte=timezone.now(), product__sub_category__category=int(request.GET['id'])).order_by("-id"), many=True)
        elif case == 8: #category buy
            serializer = self.get_serializer(Advertisement.objects.filter(visible=True, bidding_close_date__gte=timezone.now(), buy_or_sell='Buy').filter(product__sub_category__category=int(request.GET['id'])).order_by("-id"), many=True)
        elif case == 9: #category sell
            serializer = self.get_serializer(Advertisement.objects.filter(visible=True, bidding_close_date__gte=timezone.now(), buy_or_sell='Sell').filter(product__sub_category__category=int(request.GET['id'])).order_by("-id"), many=True)
        elif case == 10: #all user  addes
            serializer = self.get_serializer(Advertisement.objects.filter(user = request.user).order_by("-id"), many=True)
        elif case == 11: #Pending for approval ads
            serializer = self.get_serializer(Advertisement.objects.filter(visible = False, user=request.user).order_by("-id"), many=True)
        else:
            serializer = self.get_serializer(Advertisement.objects.all().order_by("-id"), many=True)
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
            if instance.approval:
            #check the approval
                notify = Notification(
                    heading="Bid Selected",
                    text=f"Approve the Following Advertisement on ad:id -> {instance}",
                    user=instance.selected_bid.user,
                    advertisement=instance
                )
                notify.save()

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
        serializer = self.get_serializer(Bid.objects.all().order_by("id")[:10], many=True)
        return success_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        notify_user = Advertisement.objects.get(id=request.data['advertisement']).user
        ad = Advertisement.objects.get(id=request.data['advertisement'])
        notify = Notification(
            heading="New Bid Created",
            text=f"Rs. {request.data['amount']} bidded by #{request.user.id} on ad {ad}",
            user=notify_user,
            advertisement=ad
        )
        notify.save()
        if serializer.is_valid():
            serializer.save(user=request.user)
            return success_response(serializer.data)
        return bad_request_response(serializer.errors)

@permission_classes((IsAuthenticated,))
class BidChanges(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = BidSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Bid.objects.filter(advertisement=kwargs['id']).order_by("-id")[:10] , many = True)
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
        instance = generics.get_object_or_404(BidSerializer, advertisement=kwargs['id'])
        instance.delete()
        return empty_response()
