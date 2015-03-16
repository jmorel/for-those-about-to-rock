from ftatr.common_settings import *

# keep to false for prod environment
DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'secret'

ALLOWED_HOSTS = ['.forthoseabouttorock.io', 'forthoseabouttorock.hexagonal.io']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ftatr',
        'USER': 'root',
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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

STATIC_URL = '/static/'


# Twitter
TWITTER_TOKEN = '2958240303-MGsdC8JUQX0q7VQod9fC7ieukVHbkmhVvO2VYzz'
TWITTER_TOKEN_SECRET = 'NxM84qMXS8UiP2K3SlbSgt6I8BerAR5tCQ7JeISij82ac'
TWITTER_CONSUMER_SECRET = 'Hz8wnrx6XqFC54KXvOJBax6rAZiua1jOzbTxYhlEiw7UyblOgf'
TWITTER_CONSUMER_KEY = 'sBSJX9L94dSOaG7WxX1L0SHYl'

# Facebook
FACEBOOK_APP_ID = '351060788405753'

# Admins
ADMINS = (('Jérémy', 'jeremy@forthoseabouttorock.io'), )

# Sites framework definition
SITE_ID = 1

# Email
EMAIL_HOST = ''
EMAIL_USER = ''
EMAIL_PORT = ''
EMAIL_HOST_PASSWORD = ''
