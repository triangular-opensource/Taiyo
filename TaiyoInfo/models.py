from django.db import models
from ckeditor.fields import RichTextField

from services.validators import validate_copyright, validate_email_id, validate_phone_number, validate_pincode


class Addres(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6, validators=[validate_pincode])

    def __str__(self):
        return self.address + " " + self.city + " " + self.state + " " + self.country + " " + self.pincode


class Policy(models.Model):
    terms_and_condition = RichTextField(null=False)
    privacy_policies = RichTextField(null=False)

    def __str__(self):
        return "Company policies"


class GeneralInfo(models.Model):
    name = models.CharField(max_length=50)
    icon = models.URLField(max_length=200)
    cover_image = models.URLField(max_length=200, null=True, blank=True)
    intro = models.TextField(blank=True)
    about = models.TextField(blank=True)
    email = models.EmailField(max_length=50, null=True, validators=[validate_email_id])
    contact = models.CharField(max_length=10, null=True, validators=[validate_phone_number])
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linked_in = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    android_store = models.URLField(max_length=200, null=True, blank=True)
    apple_store = models.URLField(max_length=200, null=True, blank=True)
    copyright = models.CharField(max_length=4, validators=[validate_copyright])


    def __str__(self):
        return self.name
        

class NewsLetter(models.Model):
    email = models.EmailField(max_length=50, validators=[validate_email_id])
    generation_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Subscription(models.Model):
    amount = models.CharField(max_length=30)
    days = models.CharField(max_length=100)
    def __str__(self):
        return self.amount


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, validators=[validate_email_id])
    subject = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    def __str__(self):
        return self.name