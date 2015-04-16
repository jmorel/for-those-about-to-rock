from django.shortcuts import render, get_object_or_404
from anthology.models import Manufacturer
from anthology.utils import build_index_by_name


def index(request):
    return render(request, 'manufacturer/index.html.jinja2', {
        'alphabet': build_index_by_name(Manufacturer.objects.with_published_rocking_chairs())
    })


def show(request, slug):
    manufacturer = get_object_or_404(Manufacturer, slug=slug)
    return render(request, 'manufacturer/show.html.jinja2', {
        'manufacturer': manufacturer
    })
