# Generated by Django 4.1 on 2024-04-14 18:33

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindergarten', '0019_delete_typicalday'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypicalDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('reading_bee_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='reading_bee')),
                ('activities', models.TextField()),
            ],
        ),
    ]
