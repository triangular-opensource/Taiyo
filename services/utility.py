from django.contrib import auth
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


def create_token(username, password):
    user = auth.authenticate(username=username, password=password)
    if user and user.is_verified:
        token, _ = Token.objects.get_or_create(user=user)
        return token
    return "Your email isn't verified! Please verify than try to login."


class EmaiLVerIficationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.id)+six.text_type(timestamp)+six.text_type(user.is_active))
