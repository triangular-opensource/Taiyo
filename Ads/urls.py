from django.urls import path

from Ads.views import *



urlpatterns = [
    path("advertisement", AdvertismentView.as_view(), name="advertisement"),
    path("advertisement/<int:id>", AdvertismentChanges.as_view(), name="advertisement"),
    path("add-images",AdImagesView.as_view(), name="add-images"),
    path("add-images/<int:id>",AdImagesChanges.as_view(), name="add-images"),
    path("bid", BidView.as_view(), name="bid")
]
