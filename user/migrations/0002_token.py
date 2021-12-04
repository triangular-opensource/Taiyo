# Generated by Django 3.2.3 on 2021-12-01 06:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=7)),
                ('email', models.EmailField(max_length=254)),
                ('create_time', models.DateTimeField(default=datetime.datetime(2021, 12, 1, 6, 48, 27, 625149, tzinfo=utc))),
                ('destroy_time', models.DateTimeField(default=datetime.datetime(2021, 12, 1, 6, 48, 27, 625149, tzinfo=utc))),
            ],
        ),
    ]
