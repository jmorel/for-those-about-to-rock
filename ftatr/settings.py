"""
Django settings for for_those_about_to_rock project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm_p!ki=cue6*^l6ao)=3!ek1u#j6rg6+4%n7gu6wxf-8%k+$q3'
FACEBOOK_APP_ID = '351060788405753'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.forthoseabouttorock.io', 'forthoseabouttorock.hexagonal.io']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jinja',
    'easy_thumbnails',
    'django_jinja.contrib._easy_thumbnails',
    'haystack',
    'ftatr',
    'rocking_chair',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ftatr.urls'

TEMPLATE_LOADERS = (
    'django_jinja.loaders.FileSystemLoader',
    'django_jinja.loaders.AppLoader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'ftatr.context_processors.facebook'
)

DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja2'

WSGI_APPLICATION = 'ftatr.wsgi.application'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Thumbnails
THUMBNAIL_ALIASES = {
    '': {
        # project wide target
        '540x540': {
            'size': (540, 540),
        },
        '50x50': {
            'size': (50, 50),
        }
    }
}


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ftatr',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ftatr/static'),
)

# Media files (user uploaded)
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

# WARNING
# this needs to be at the very end of the file so that variables are overriden
try:
    from ftatr.settings_local import *
except ImportError:
    pass
