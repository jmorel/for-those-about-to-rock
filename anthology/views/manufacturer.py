from django.shortcuts import render, get_object_or_404
from anthology.models import Manufacturer
from anthology.utils import build_index_by_name


def index(request):
    return render(request, 'manufacturer/index.html.jinja2', {
        # SEM metas
        'title': 'Rocking chairs\' manufacturers',
        'description': """A collection of all manufacturers who ever built rocking chairs, alphabetically ordered.""",
        # Page content
        'alphabet': build_index_by_name(Manufacturer.objects.with_published_rocking_chairs())
    })


def show(request, slug):
    manufacturer = get_object_or_404(Manufacturer, slug=slug)
    return render(request, 'manufacturer/show.html.jinja2', {
        # SEM metas
        'title': "{manufacturer} (rocking chair manufacturer)".format(manufacturer=manufacturer.name),
        'description': """More details about the manufacturer {manufacturer} and rocking chairs it builds and sells""".format(manufacturer=manufacturer.name),
        'image': manufacturer.logo.url if manufacturer.logo else None,
        # Page content
        'manufacturer': manufacturer
    })
