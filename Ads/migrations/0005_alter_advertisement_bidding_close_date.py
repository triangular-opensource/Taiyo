# Generated by Django 3.2.3 on 2022-01-16 06:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0004_alter_advertisement_bidding_close_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='bidding_close_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 31, 6, 13, 13, 486274, tzinfo=utc)),
        ),
    ]
