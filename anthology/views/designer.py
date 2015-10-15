from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static
from anthology.models import Designer
from anthology.utils import build_index_by_name


def index(request):
    return render(request, 'designer/index.html.jinja2', {
        # SEM metas
        'title': 'Rocking chairs\' designers',
        'description': """A collection of all designers who ever designed (but not always managed to get manufactured,
        though at least a physical prototype is required to be listed here) rocking chairs, alphabetically ordered.""",
        'image': static('ftatr/images/designer-yellow-bg.png'),
        # Page content
        'alphabet': build_index_by_name(Designer.objects.with_published_rocking_chairs(), attribute='last_name')
    })


def show(request, slug):
    designer = get_object_or_404(Designer, slug=slug)

    return render(request, 'designer/show.html.jinja2', {
        # SEM metas
        'title': "{designer} (rocking chair designer)".format(designer=designer.full_name),
        'description': """More details about the designer {designer} and his/her career designing rocking chairs.""".format(designer=designer.full_name),
        'image': designer.portrait.url if designer.portrait else static('ftatr/images/designer-yellow-bg.png'),
        # Page content
        'designer': designer
    })
