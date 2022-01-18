from datetime import timedelta
from email.policy import default
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from django.conf import settings

from services.constant import AD_QUALITY, AD_TEMPER,  BUY_OR_SELL
from features.models import Product
from services.mailing import send_email
from services.validators import validate_phone_number
from django.core.validators import MinValueValidator

User = get_user_model()


class Advertisement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_description = models.TextField()
    buy_or_sell = models.CharField(max_length=4, choices=BUY_OR_SELL)
    basic_price = models.FloatField(validators=[MinValueValidator(9999)])
    excel_file = models.FileField(null=True, blank=True)
    excel_file_link = models.URLField(max_length=300, null=True, blank=True)
    pdf_file = models.FileField(null=True, blank=True)
    pdf_file_link = models.URLField(max_length=300, null=True, blank=True)
    image_1 = models.FileField(null=True , blank=True)
    image_1_link = models.URLField(max_length=300)
    image_2 = models.FileField(null=True, blank=True)
    image_2_link = models.URLField(max_length=300, null=True, blank=True)
    image_3 = models.FileField(null=True, blank=True)
    image_3_link = models.URLField(max_length=300, null=True, blank=True)
    image_4 = models.FileField(null=True, blank=True)
    image_4_link = models.URLField(max_length=300, null=True, blank=True) 
    quality = models.CharField(max_length=10, choices=AD_QUALITY, null=True, blank=True)
    temper = models.CharField(max_length=4, choices=AD_TEMPER, null=True, blank=True)
    dimensions = models.CharField(max_length=100, null=True, blank=True)
    grade = models.CharField(max_length=50, null=True, blank=True)
    specification_number = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    coating_in_gsm = models.CharField(max_length=30, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    bidding = models.BooleanField(default=True)
    bidding_close_date = models.DateTimeField(default=(timezone.now() + timedelta(days=15)))
    selected_bid = models.ForeignKey('Ads.Bid', on_delete=models.DO_NOTHING, null=True, blank=True, related_name="winning_bid")
    approval = models.BooleanField(default=False , blank=True , null = True)

    ## author information

    name = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=10, validators=[validate_phone_number])
    business_address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    #creater
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by", null=True)
    #location edit
    latitude = models.FloatField(max_length=50, blank=True, null=True)
    longitude = models.FloatField(max_length=50, blank=True, null=True)
    visible = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    #email sending
    subject = models.CharField(max_length=100 , blank=True , null=True)
    message = models.TextField(blank=True , null=True)


    @property
    def category(self):
        return self.product.category
   
    def image_1_display(self):
        if self.image_1_link:
            return mark_safe(f'<img src="{self.image_1_link}" width="auto" height="150px" />')
        return mark_safe('<span id="image_1_display">No image selected!</span>')
    
    def image_2_display(self):
        if self.image_2_link:
            return mark_safe(f'<img src="{self.image_2_link}" width="auto" height="150px" />')
        return mark_safe('<span id="image_2_display">No image selected!</span>')
    
    def image_3_display(self):
        if self.image_3_link:
            return mark_safe(f'<img src="{self.image_3_link}" width="auto" height="150px" />')
        return mark_safe('<span id="image_3_display">No image selected!</span>')
    
    def image_4_display(self):
        if self.image_4_link:
            return mark_safe(f'<img src="{self.image_4_link}" width="auto" height="150px" />')
        return mark_safe('<span id="image_4_display">No image selected!</span>')

    def __str__(self):
        return f"#{self.id}"

    def save(self, *args, **kwargs):
        if self.selected_bid:
            send_email("Taiyo : Approval Of Bid",
                       f''' 
                       **** Taiyo industries recommend you to deal with the bidder carefully to avoid frauds. ****
                       **** Taiyo is not responsible for any miscondut in it. ****
                        verify this add..... 
                        visit the AD-ID : {self.id} '''
                       ,
                       self.selected_bid.user.email)
        super(Advertisement, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.subject and self.message:
            send_email(self.subject,self.message,
                       self.user.email)
        super(Advertisement, self).delete(*args, **kwargs)



class Bid(models.Model):
    amount = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, null=True)
    selected = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.amount) +" "+ str(self.user)


