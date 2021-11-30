from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.URLField(blank=True, null=True, max_length=255)

    middle_name = models.charField(max_length=True)
    gst_number = models.CharField(required=True, max_length=16)
    phone_number = models.CharField(required=True, max_length=16)

    company_name = models.CharField(required=True, max_length=50)
    company_type = models.CharField(required=True, max_length=30)
    company_address = models.CharField(required=True, max_length=50)
    company_city = models.CharField(required=True, max_length=50)
    company_state = models.CharField(required=True, max_length=50)
    company_country = models.CharField(required=True, max_length=50)
    company_pin_code = models.CharField(required=True, max_length=50)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
