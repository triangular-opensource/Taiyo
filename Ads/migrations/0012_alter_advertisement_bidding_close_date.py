# Generated by Django 3.2.3 on 2022-01-26 07:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0011_alter_advertisement_bidding_close_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='bidding_close_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 7, 31, 26, 940571, tzinfo=utc)),
        ),
    ]
