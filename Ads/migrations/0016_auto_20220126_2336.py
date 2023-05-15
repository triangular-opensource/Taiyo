# Generated by Django 3.2.3 on 2022-01-26 18:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0015_alter_advertisement_bidding_close_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='bidding_close_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 18, 6, 44, 363896, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 18, 6, 44, 364896, tzinfo=utc)),
        ),
    ]
