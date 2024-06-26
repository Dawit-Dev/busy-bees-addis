from django.db import models
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField


class Hero(models.Model):
    logo = CloudinaryField('logo')
    hero_image = CloudinaryField('hero_image')
    brand = models.CharField(max_length=255)
    motto = models.CharField(max_length=255)


class Program(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()


class TypicalDay(models.Model):
    title = models.CharField(max_length=255)
    reading_bee_image = CloudinaryField('reading_bee')
    activities = models.TextField()


class Feature(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    icon_name = models.CharField(max_length=55)


class CompoundImage(models.Model):
    compound_image = CloudinaryField('compound_image')
    caption = models.CharField(max_length=255, default='')


class OpenHouseImage(models.Model):
    open_house_image = CloudinaryField('open_house_image')
    caption = models.CharField(max_length=255, default='')


# Image upload to local directory
# class OpenHouseImage(models.Model):
#     open_house_image = models.ImageField(upload_to='images/open-house/')
#     caption = models.CharField(max_length=255, default='')


class Team(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = CloudinaryField('image')
    about = models.TextField()


class Contact(models.Model):
    street = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    country = models.CharField(max_length=55)
    phone_number_1 = models.CharField(max_length=55)
    phone_number_2 = models.CharField(max_length=55)
    phone_number_3 = models.CharField(max_length=55)
    image = CloudinaryField('image')
    facebook = models.CharField(max_length=255, default='')
    instagram = models.CharField(max_length=255, default='')


class Register(models.Model):
    title = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=55)
    requirements = models.TextField()
