from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


class Addres(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.address + " " + self.city + " " + self.state + " " + self.country + " " + self.pincode


class Policy(models.Model):
    terms_and_condition = RichTextField(null=False)
    privacy_policies = RichTextField(null=False)

    def __str__(self):
        return "Company policies"


class GenralInfo(models.Model):
    name = models.CharField(max_length=50)
    icon = models.URLField(max_length=200)
    cover_image = models.URLField(max_length=200, null=True, blank=True)
    intro = models.TextField(blank=True)
    about = models.TextField(blank=True)
    email = models.EmailField(max_length=50, default='')
    contact = models.CharField(max_length=10, default='')
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linked_in = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    android_store = models.URLField(max_length=200, null=True, blank=True)
    apple_store = models.URLField(max_length=200, null=True, blank=True)
    copyright = models.CharField(max_length=4)
    address = models.OneToOneField(Addres, on_delete=models.CASCADE)
    policies = models.OneToOneField(Policy, on_delete=models.CASCADE)
    models.TextField(blank=True)
    def __str__(self):
        return self.title


class NewsLetter(models.Model):
    email = models.EmailField(max_length=50)
    generation_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
