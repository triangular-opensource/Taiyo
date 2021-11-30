from django.urls import path

from TaiyoInfo.views import GeneralInfoView

urlpatterns = [
    path("general-info", GeneralInfoView.as_view(), name="general-info"),
    path("general-info", GeneralInfoView.as_view(), name="address"),
    path("policy", GeneralInfoView.as_view(), name="policy"),
    path("news-letter", GeneralInfoView.as_view(), name="news-letter")
]
