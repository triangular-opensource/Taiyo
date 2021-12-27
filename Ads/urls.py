from django.urls import path

from Ads.views import *


urlpatterns = [
    path("ads/<int:id>", AdvertismentView.as_view(), name="advertisement"),
    path("post-ads", AdvertisementPostView.as_view(), name="advertisement post"),
    path("ads/<int:id>", AdvertismentChanges.as_view(), name="advertisement"),
    path("ads/bid", BidView.as_view(), name="bid"),
    path("ads/bid/<int:id>", BidChanges.as_view(), name="bid")
]
