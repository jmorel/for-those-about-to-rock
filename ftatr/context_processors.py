from . import settings


def facebook(request):
    return {
        'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID
    }