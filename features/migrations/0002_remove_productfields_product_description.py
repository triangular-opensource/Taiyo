# Generated by Django 3.2.3 on 2022-01-16 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfields',
            name='product_description',
        ),
    ]
