from django_jinja import library
from ftatr import settings


@library.global_function()
def settings_value(name):
    return getattr(settings, name, "")
