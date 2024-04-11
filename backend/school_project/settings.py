"""
Django settings for school_project project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from os import environ
import urllib.parse as up
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env')
MEDIA_ROOT = os.path.join(BASE_DIR, '../../frontend/public')
MEDIA_URL = '../../frontend/public/'
# vercel
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles", "static")
# STATIC_ROOT = os.path.join(BASE_DIR, "frontend/public")
# STATIC_URL = "public/"
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "frontend/public")]
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATIC_URL = "static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "frontend/public")]
# STATIC_URL = "/public/"
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "frontend/public")]

# STATIC_ROOT = os.path.join(BASE_DIR, "frontend/public")
# STATIC_ROOT = os.path.join(BASE_DIR, "frontend/public")


# Parsing database url
up.uses_netloc.append('postgres')
url = up.urlparse(environ.get('DATABASE_URL'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = environ.get("DEBUG") != "False"


ALLOWED_HOSTS = [
    '127.0.0.1',
    'http://localhost:8000',
    'localhost',
    '.vercel.app',
    '.now.sh',
]

# vercel_app/settings.py
WSGI_APPLICATION = 'vercel_app.wsgi.app'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third apps
    'rest_framework',
    'whitenoise.runserver_nostatic',
    # installed apps
    'kindergarten',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'school_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'school_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = 'static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "backend/kindergarten/static")]
# STATIC_URL = "static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "backend/kindergarten/staticfiles")
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATIC_URL = "static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# PROJECT_ROOT = Path(__file__).resolve().parent.parent
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = 'static/'

# STATICFILES_DIRS = [BASE_DIR / 'static']

# STATIC_ROOT = BASE_DIR / 'staticfiles'

# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
