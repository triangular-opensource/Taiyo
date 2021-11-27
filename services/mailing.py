from django.conf import settings
from django.core.mail import send_mail



from django.core.mail import send_mail
from django.template.loader import render_to_string



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



def sendNewsEmail(newsList):
    msg_html = render_to_string('templates/email.html', {'some_params': newsList})
    send_mail(
        'email title',
        msg_html,
        'some@sender.com',
        ['some@receiver.com'],
        html_message=msg_html,
    )

