from django.urls import path

from TaiyoInfo.views import GeneralInfoView

urlpatterns = [
    path("general-info", GeneralInfoView.as_view(), name="general-info"),
]
