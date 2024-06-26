# Generated by Django 4.1 on 2024-04-14 21:26

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindergarten', '0027_delete_address_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=55)),
                ('city', models.CharField(max_length=55)),
                ('country', models.CharField(max_length=55)),
                ('phone_number_1', models.CharField(max_length=55)),
                ('phone_number_2', models.CharField(max_length=55)),
                ('phone_number_3', models.CharField(max_length=55)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('facebook', models.CharField(default='', max_length=255)),
                ('instagram', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('subtitle', models.CharField(max_length=55)),
                ('requirements', models.TextField()),
            ],
        ),
    ]
