# Generated by Django 3.2.3 on 2021-12-28 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TaiyoInfo', '0001_initial'),
        ('payment', '0002_payment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='TaiyoInfo.subscription'),
        ),
    ]
