# Generated by Django 3.2.3 on 2022-01-16 19:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0008_auto_20220117_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='bidding_close_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 31, 19, 24, 31, 990655, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='image_1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
