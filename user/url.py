urlpatterns = [
    path('register', RegisterAPI.as_view(), name="register"),
    path('login', LoginAPIView.as_view(), name="login"),
]