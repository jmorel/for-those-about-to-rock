import datetime
from django.shortcuts import render, get_object_or_404
from anthology.models import Designer
from anthology.utils import build_index_by_name


def index(request):
    designers = Designer.objects \
        .exclude(rocking_chairs=None) \
        .exclude(rocking_chairs__published_at__gte=datetime.datetime.now()) \
        .order_by('last_name')
    return render(request, 'designer/index.html.jinja2', {
        'alphabet': build_index_by_name(designers, attribute='last_name')
    })


def show(request, slug):
    designer = get_object_or_404(Designer, slug=slug)
    return render(request, 'designer/show.html.jinja2', {
        'designer': designer
    })
