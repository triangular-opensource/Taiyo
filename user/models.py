from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from services.constant import COMPANY_TYPE
from services.validators import validate_gst_number, validate_phone_number, validate_pincode


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, default="", blank=True, null=True)
    last_name = models.CharField(max_length=30)
    image = models.URLField(blank=True, default="https://firebasestorage.googleapis.com/v0/b/taiyo-768b4.appspot.com/o/Users%2Fdefault.png?alt=media&token=4fdd5a7a-cb6c-41c5-bcfc-5b95352a64bf", null=True, max_length=255)
    gst_number = models.CharField(max_length=15, validators=[validate_gst_number])
    phone_number = models.CharField(max_length=10, validators=[validate_phone_number])

    user_type = models.CharField(max_length=20)
    package_type = models.CharField(max_length=10)
    package_expiry = models.DateTimeField(default=timezone.now)

    company_name = models.CharField(max_length=50)
    company_type = models.CharField(max_length=30, choices=COMPANY_TYPE)
    company_address = models.CharField(max_length=50)
    company_city = models.CharField(max_length=50)
    company_state = models.CharField(max_length=50)
    company_country = models.CharField(max_length=50)
    company_pin_code = models.CharField(max_length=6, validators=[validate_pincode])

    friends = models.ManyToManyField("self", blank=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

class Token(models.Model):
    token = models.CharField(max_length=7 , blank=False , null = False)
    email = models.EmailField(null=False)
    create_time = models.DateTimeField(auto_now=True)
    destroy_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.token

    def save(self, *args , **kwargs):
        if self.create_time:
            self.destroy_time = self.create_time + timedelta(minutes=3)
        super(Token, self).save(*args, **kwargs)






class Notification(models.Model):
    heading = models.CharField(max_length=300)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


