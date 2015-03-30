from django.shortcuts import render, get_object_or_404
from rocking_chair.models import Manufacturer
from rocking_chair.utils import build_index_by_name


def index(request):
    manufacturers = Manufacturer.objects \
        .exclude(rocking_chairs=None) \
        .order_by('name')
    return render(request, 'manufacturer/index.html.jinja2', {
        'alphabet': build_index_by_name(manufacturers)
    })


def show(request, slug):
    manufacturer = get_object_or_404(Manufacturer, slug=slug)
    return render(request, 'manufacturer/show.html.jinja2', {
        'manufacturer': manufacturer
    })
