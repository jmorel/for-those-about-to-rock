"""
Django settings for for_those_about_to_rock project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from distutils.util import strtobool
import os

import dj_database_url

DEBUG = strtobool(os.environ.get('DEBUG', 'False'))
TEMPLATE_DEBUG = strtobool(os.environ.get('TEMPLATE_DEBUG', 'False'))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # static files: cloudinary_storage must be before django.contrib.staticfiles
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    # end static files
    'easy_thumbnails',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'haystack',
    'ftatr',
    'anthology',
    'compressor',

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            os.path.join(BASE_DIR, 'jinja2'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'ftatr.jinja2.environment'
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                # default context processors
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # custom context processors
                'django.template.context_processors.request', # for django-suit
            ],
        }
    },
]

WSGI_APPLICATION = 'ftatr.wsgi.application'


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
    ('text/less', '%(less)s --include-path="%(project_path)s:%(less_include_paths)s" {infile} {outfile} && %(autoprefixer)s --use autoprefixer {outfile}' % {
        'less': os.path.join(BASE_DIR, 'node_modules/less/bin/lessc'),
        'project_path': BASE_DIR,
        'less_include_paths': os.path.join(BASE_DIR, 'ftatr'),
        'autoprefixer': os.path.join(BASE_DIR, 'node_modules/postcss-cli/bin/postcss'),
    }),
)
COMPRESS_OUTPUT_DIR = 'compressed'
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False


SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['.forthoseabouttorock.io', 'forthoseabouttorock.hexagonal.io']

DATABASES = {
    'default': dj_database_url.config()
}

# Static files
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

# Media files
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Twitter
TWITTER_TOKEN = os.environ.get('TWITTER_TOKEN')
TWITTER_TOKEN_SECRET = os.environ.get('TWITTER_TOKEN_SECRET')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')

# Facebook
FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')

# Admins
ADMINS = (('Jérémy', 'jeremy@forthoseabouttorock.io'), )

# Sites framework definition
SITE_ID = 1

# Email
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
SERVER_EMAIL = 'noreply@forthoseabouttorock.io'

# reCaptcha
RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')
RECAPTCHA_SITE_KEY = os.environ.get('RECAPTCHA_SITE_KEY')
