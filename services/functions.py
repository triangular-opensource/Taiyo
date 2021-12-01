from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from services.utility import EmaiLVerIficationTokenGenerator
from django.core.mail import EmailMessage

User = get_user_model()
generate_token = EmaiLVerIficationTokenGenerator()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    subject = "Activate your HighOnCode Accout"
    body = render_to_string("activate.html", {
        "user": user,
        "domain": current_site,
        "uid": urlsafe_base64_encode(force_bytes(user.id)),
        "token": generate_token.make_token(user)
    })

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.EMAIL_FROM_USER,
        to=[user.email]
    )

    email.send()
