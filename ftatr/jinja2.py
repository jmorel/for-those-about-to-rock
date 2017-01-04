from compressor.contrib.jinja2ext import CompressorExtension
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from easy_thumbnails.templatetags.thumbnail import thumbnail_url

from anthology.templatetags.contribution import contribution_form
from anthology.templatetags.nav import nav
from ftatr.templatetags.absolute import absolute
from ftatr.templatetags.settings_constant import settings_value

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.add_extension(CompressorExtension)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': url,
        'nav': nav,
        'contribution_form': contribution_form,
        'settings_value': settings_value,
    })
    env.filters.update({
        'thumbnail_url': thumbnail_url,
        'absolute': absolute,
    })
    return env


def url(route, **kwargs):
    return reverse(route, kwargs=kwargs)
