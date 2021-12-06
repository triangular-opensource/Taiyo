from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from services.newsletterdata import generateNewsData


def send_email(subject, message, to):
    return send_mail(
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



def sendNewsEmail(email):
    response = generateNewsData()
    print(response)
    msg_html = render_to_string('email/email.html', {'data': response})
    send_mail(
        'Taiyo : NewsLetter',
        msg_html,
        "taiyo.apex@gmail.com",
        [email],
        html_message=msg_html,
    )




def sendContactEmail(response):
    msg_html = render_to_string('email/contact.html', {'data': response})
    send_mail(
        'Taiyo : SomeOne Wants To  COntact',
        msg_html,
        "taiyo.apex@gmail.com",
        ['taiyo.apex@gmail.com'],
        html_message=msg_html,
    )


