import datetime
from django.shortcuts import render, get_object_or_404
from anthology.models import Manufacturer
from anthology.utils import build_index_by_name


def index(request):
    manufacturers = Manufacturer.objects \
        .exclude(rocking_chairs=None) \
        .exclude(rocking_chairs__published_at__gte=datetime.datetime.now()) \
        .order_by('name')
    return render(request, 'manufacturer/index.html.jinja2', {
        'alphabet': build_index_by_name(manufacturers)
    })


def show(request, slug):
    manufacturer = get_object_or_404(Manufacturer, slug=slug)
    return render(request, 'manufacturer/show.html.jinja2', {
        'manufacturer': manufacturer
    })
