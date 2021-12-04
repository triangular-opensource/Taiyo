from django.urls import path

from Ads.views import



urlpatterns = [
    path("advertisement",.as_view(), name="advertisement"),
    path("add-images",.as_view(), name="add-images"),
    path("bid", .as_view(), name="bid")
]
