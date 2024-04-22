# Generated by Django 4.1 on 2024-04-12 21:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindergarten', '0011_address_facebook_address_instagram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('subtitle', models.CharField(max_length=55)),
                ('requirements', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), default=list, size=20)),
            ],
        ),
    ]
