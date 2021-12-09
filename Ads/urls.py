from django.urls import path

from Ads.views import *


urlpatterns = [
    path("ads", AdvertismentView.as_view(), name="advertisement"),
    path("ads/<int:id>", AdvertismentChanges.as_view(), name="advertisement"),
    path("ads/bid", BidView.as_view(), name="bid"),
    path("ads/bid/<int:id>", BidChanges.as_view(), name="bid")
]
