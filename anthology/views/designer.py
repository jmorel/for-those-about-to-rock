from django.shortcuts import render, get_object_or_404
from anthology.models import Designer
from anthology.utils import build_index_by_name


def index(request):
    return render(request, 'designer/index.html.jinja2', {
        'alphabet': build_index_by_name(Designer.objects.with_published_rocking_chairs(), attribute='last_name')
    })


def show(request, slug):
    designer = get_object_or_404(Designer, slug=slug)
    return render(request, 'designer/show.html.jinja2', {
        'designer': designer
    })
