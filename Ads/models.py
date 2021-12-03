from django.db import models
from django.utils import timezone

from services.constant import AD_QUALITY, AD_TEMPER,  BUY_OR_SELL
from TaiyoInfo.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()




class Advertisement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    buy_or_sell = models.CharField(max_length=4, choices=BUY_OR_SELL)
    basic_price = models.FloatField()
    excel_file = models.URLField(max_length=300, null=True, blank=True)
    quality = models.CharField(max_length=10, choices=AD_QUALITY)
    thickness = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    grade_or_spec = models.CharField(max_length=50)
    temper = models.CharField(max_length=4, choices=AD_TEMPER)
    specification_number = models.CharField(max_length=20)
    quantity = models.IntegerField()
    coating_in_gsm = models.CharField(max_length=30)
    product_description = models.TextField()
    bidding = models.BooleanField()
    bidding_close_date = models.DateTimeField(default=timezone.now)
    author_name = models.CharField(max_length=40)
    author_mobile_name = models.CharField(max_length=10)
    author_contry = models.CharField(max_length=20)
    author_buisness_address = models.CharField(max_length=100)


    @property
    def category(self):
        return self.product.category

    def __str__(self):
        return self.product.name




class AdImages(models.Model):
    image = models.URLField(max_length=300, null=True, blank=True)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.image




class Bid(models.Model):
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, null=True)
    selected = models.BooleanField(default=False)
    def __str__(self):
        return str(self.amount) +" "+ self.user.username


