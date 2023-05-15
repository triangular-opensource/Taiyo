# Generated by Django 3.2.3 on 2022-01-16 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ads', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='features.product'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='selected_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='winning_bid', to='Ads.bid'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
