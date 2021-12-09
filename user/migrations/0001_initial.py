# Generated by Django 3.2.3 on 2021-12-08 08:55

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import services.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=7)),
                ('email', models.EmailField(max_length=254)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('destroy_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('image', models.URLField(blank=True, max_length=255, null=True)),
                ('gst_number', models.CharField(max_length=16)),
                ('phone_number', models.CharField(max_length=16, validators=[services.validators.validate_phone_number])),
                ('user_type', models.CharField(max_length=20)),
                ('package_type', models.CharField(max_length=10)),
                ('package_expiry', models.DateTimeField(default=django.utils.timezone.now)),
                ('company_name', models.CharField(max_length=50)),
                ('company_type', models.CharField(choices=[('Proprietorship', 'Proprietorship'), ('Partnership', 'Partnership'), ('Pvt Ltd', 'PvtLtd'), ('Ltd', 'Ltd'), ('LLP', 'LLP')], max_length=30)),
                ('company_address', models.CharField(max_length=50)),
                ('company_city', models.CharField(max_length=50)),
                ('company_state', models.CharField(max_length=50)),
                ('company_country', models.CharField(max_length=50)),
                ('company_pin_code', models.CharField(max_length=6, validators=[services.validators.validate_pincode])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
