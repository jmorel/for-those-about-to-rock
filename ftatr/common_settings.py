"""
Django settings for for_those_about_to_rock project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
from django_jinja.builtins import DEFAULT_EXTENSIONS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jinja',
    'easy_thumbnails',
    'django_jinja.contrib._easy_thumbnails',
    'compressor',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'haystack',
    'ftatr',
    'anthology',
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
    'django.template.loaders.app_directories.Loader',
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
        },
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
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ftatr/static'),
)

# Asset manager (django-compressor)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/less', 'node_modules/less/bin/lessc {infile} {outfile} && node_modules/postcss-cli/bin/postcss --use autoprefixer {outfile}'),
)
COMPRESS_OUTPUT_DIR = 'compressed'
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False

JINJA2_EXTENSIONS = DEFAULT_EXTENSIONS + [
    'compressor.contrib.jinja2ext.CompressorExtension',
]
