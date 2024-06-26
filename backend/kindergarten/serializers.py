from django.contrib.auth.models import User, Group

from rest_framework import serializers

from kindergarten.models import (
    Hero,
    Program,
    TypicalDay,
    Feature,
    CompoundImage,
    OpenHouseImage,
    Team,
    Contact,
    Register,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = [
            'id',
            'url',
            'logo',
            'hero_image',
            'brand',
            'motto',
        ]
        read_only_fields = ['id']


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        fields = [
            'id',
            'url',
            'title',
            'content',
        ]
        read_only_fields = ['id']


class TypicalDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypicalDay
        fields = [
            'id',
            'url',
            'title',
            'reading_bee_image',
            'activities',
        ]
        read_only_fields = ['id']


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feature
        fields = [
            'id',
            'url',
            'title',
            'description',
            'icon_name',
        ]
        read_only_fields = ['id']


class CompoundImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompoundImage
        fields = [
            'id',
            'url',
            'compound_image',
            'caption',
        ]
        read_only_fields = ['id']


class OpenHouseImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenHouseImage
        fields = [
            'id',
            'url',
            'open_house_image',
            'caption',
        ]
        read_only_fields = ['id']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = [
            'id',
            'url',
            'name',
            'position',
            'image',
            'about',
        ]
        read_only_fields = ['id']


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'url',
            'street',
            'city',
            'country',
            'phone_number_1',
            'phone_number_2',
            'phone_number_3',
            'image',
            'facebook',
            'instagram',
        ]
        read_only_fields = ['id']


class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Register
        fields = [
            'id',
            'url',
            'title',
            'subtitle',
            'requirements',
        ]
        read_only_fields = ['id']
