from django.conf import settings
from django.core.mail import send_mail


def send_email(subject, message, to):
    return
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to],
        fail_silently=False,
        auth_user=None,
        auth_password=None,
        connection=None,
        html_message=None
    )
