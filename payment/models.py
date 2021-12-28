from django.db import models

from django.contrib.auth import get_user_model
from TaiyoInfo.models import Subscription

User = get_user_model()


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    order_id = models.CharField(max_length=50)
    payment_id = models.CharField(max_length=50)
    payment_signature = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    package = models.ForeignKey(Subscription, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.id}"