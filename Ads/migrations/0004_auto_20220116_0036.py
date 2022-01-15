# Generated by Django 3.2.3 on 2022-01-15 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0003_auto_20220116_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='dimentions',
            new_name='dimensions',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='bidding_close_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 30, 19, 6, 1, 854649, tzinfo=utc)),
        ),
    ]
