from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import BigAutoField
from django.utils import timezone
from django.utils.html import mark_safe

from services.constant import AD_QUALITY, AD_TEMPER,  BUY_OR_SELL
from TaiyoInfo.models import Product

User = get_user_model()


class Advertisement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    buy_or_sell = models.CharField(max_length=4, choices=BUY_OR_SELL)
    basic_price = models.FloatField()
    excel_file = models.URLField(max_length=300, null=True, blank=True)
    pdf_file = models.URLField(max_length=300, null=True, blank=True)
    image_1 = models.FileField(null=True, blank=True)
    image_1_link = models.URLField(max_length=300, null=True, blank=True)
    image_2 = models.FileField(null=True, blank=True)
    image_2_link = models.URLField(max_length=300, null=True, blank=True)
    image_3 = models.FileField(null=True, blank=True)
    image_3_link = models.URLField(max_length=300, null=True, blank=True)
    image_4 = models.FileField(null=True, blank=True)
    image_4_link = models.URLField(max_length=300, null=True, blank=True)
    quality = models.CharField(max_length=10, choices=AD_QUALITY)
    thickness = models.FloatField()
    width = models.FloatField()
    length = models.FloatField()
    grade_or_spec = models.CharField(max_length=50)
    temper = models.CharField(max_length=4, choices=AD_TEMPER)
    specification_number = models.CharField(max_length=20)
    quantity = models.IntegerField()
    coating_in_gsm = models.CharField(max_length=30)
    product_description = models.TextField()
    bidding = models.BooleanField()
    bidding_close_date = models.DateTimeField(default=timezone.now)
    author_name = models.CharField(max_length=40)
    author_mobile_number = models.CharField(max_length=10)
    author_country = models.CharField(max_length=20)
    author_business_address = models.CharField(max_length=100)

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
        return str(self.id)


class Bid(models.Model):
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, null=True)
    selected = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.amount) +" "+ str(self.user)


