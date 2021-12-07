# Generated by Django 3.2.3 on 2021-12-07 06:44

from django.db import migrations, models
import services.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211206_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company_pin_code',
            field=models.CharField(max_length=6, validators=[services.validators.validate_pincode]),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=16, validators=[services.validators.validate_phone_number]),
        ),
    ]
