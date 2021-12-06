from django.urls import path

from TaiyoInfo.views import GeneralInfoView, AddressView, PolicyView, NewsLetterView , ContactView

urlpatterns = [
    path("general-info", GeneralInfoView.as_view(), name="general-info"),
    path("address", AddressView.as_view(), name="address"),
    path("policy", PolicyView.as_view(), name="policy"),
    path("news-letter", NewsLetterView.as_view(), name="news-letter"),
    path("subscription", NewsLetterView.as_view(), name="subscription"),
    path("contact", ContactView.as_view(), name="subscription")
]
