from django.contrib import auth
from rest_framework.authtoken.models import Token


def create_token(email, password):
    user = auth.authenticate(username=email, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return token
