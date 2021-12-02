from django.db import models
from django.utils import timezone

from services.constant import AD_QUALITY, AD_TEMPER, ADS_CATEGORY, BUY_OR_SELL


class Category(models.Model):
    name = models.CharField(max_length=20, choices=ADS_CATEGORY)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Advertisement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    buy_or_sell = models.CharField(max_length=4, choices=BUY_OR_SELL)
    basic_price = models.FloatField()
    image = models.URLField(max_length=300, null=True, blank=True)
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
    
