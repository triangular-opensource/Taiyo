from django.db import models
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField

from services.validators import validate_copyright, validate_email_id, validate_phone_number, validate_pincode


class Addres(models.Model):
    address = models.CharField(max_length=100)
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

    class Meta:
        verbose_name = "Policie"


class GeneralInfo(models.Model):
    name = models.CharField(max_length=50)
    icon = models.FileField(null=True)
    icon_link = models.URLField(max_length=300, null=True, blank=True)
    cover_image = models.FileField(null=True)
    cover_image_link = models.URLField(max_length=200, null=True, blank=True)
    intro = models.TextField(blank=True)
    about = models.TextField(blank=True)
    email = models.EmailField(max_length=50, null=True, validators=[validate_email_id])
    phone_number = models.CharField(max_length=10, null=True, validators=[validate_phone_number])
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linked_in = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    android_store = models.URLField(max_length=200, null=True, blank=True)
    apple_store = models.URLField(max_length=200, null=True, blank=True)
    copyright = models.CharField(max_length=4, validators=[validate_copyright])

    def icon_tag(self):
        if self.icon:
            return mark_safe(f'<img src="{self.icon}" width="auto" height="150px" />')
        return mark_safe('<span id="icon_display">No image selected!</span>')
    
    def cover_tag(self):
        if self.cover_image:
            return mark_safe(f'<img src="{self.cover_image}" width="auto" height="150" />')
        return mark_safe('<span id="cover_display">No image selected!</span>')

    icon_tag.short_description = 'Icon Preview'
    cover_tag.short_description = 'Cover Preview'

    def __str__(self):
        return self.name
        

class NewsLetter(models.Model):
    email = models.EmailField(max_length=50, validators=[validate_email_id])
    generation_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email



class Subscription(models.Model):
    name = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)
    days = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, validators=[validate_email_id])
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name