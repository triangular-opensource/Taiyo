# Generated by Django 3.2.3 on 2022-01-26 07:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0009_auto_20220117_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='bidding_close_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 7, 14, 36, 730892, tzinfo=utc)),
        ),
    ]
