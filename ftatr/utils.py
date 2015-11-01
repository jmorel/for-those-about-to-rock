import requests
from ftatr.settings import RECAPTCHA_SECRET_KEY


def is_recaptcha_valid(request):
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', {
        'secret': RECAPTCHA_SECRET_KEY,
        'response': request.POST.get('g-recaptcha-response', ''),
        'remoteip': _get_remote_ip(request),
    })

    return response.json().get('success')


def _get_remote_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
