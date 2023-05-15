from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from services.newsletterdata import generateNewsData
from services.utility import EmaiLVerIficationTokenGenerator
from django.core.mail import EmailMessage, send_mail

from TaiyoInfo.models import NewsLetter

User = get_user_model()
generate_token = EmaiLVerIficationTokenGenerator()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    subject = "Activate your Taiyo Accout"
    body = render_to_string("activate.html", {
        "user": user,
        "domain": current_site,
        "uid": urlsafe_base64_encode(force_bytes(user.id)),
        "token": generate_token.make_token(user)
    })

    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [user.email],
        html_message=body
    )

def sendNewsEmail(email):
    response = generateNewsData()
    msg_html = render_to_string('email/email.html', {'data': response})
    send_mail(
        'Taiyo : NewsLetter',
        msg_html,
        "taiyo.apex@gmail.com",
        [email],
        html_message=msg_html,
    )

def send_newsletter():
    users = NewsLetter.objects.all()
    for user in users:
        sendNewsEmail(user.email)
