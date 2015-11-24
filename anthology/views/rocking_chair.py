from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from anthology.models import RockingChair
from anthology.utils import build_index_by_name, build_index_by_year


def index(request):
    # prepare general request
    rocking_chairs = RockingChair.objects.published().order_by('-published_at')
    # set up paginator
    paginator = Paginator(rocking_chairs, 10)
    page = request.GET.get('page')
    try:
        paged_rocking_chairs = paginator.page(page)
    except PageNotAnInteger:
        paged_rocking_chairs = paginator.page(1)
    except EmptyPage:
        paged_rocking_chairs = paginator.page(paginator.num_pages)

    html = render_to_string('rocking_chair/index.html.jinja2', {
        # SEM metas
        'description': """For Those About To Rock is an anthology of modern rocking chair. Every day a new rocking chair
        is posted, with both gorgeous images and full details about its designer(s), manufacturer(s) etc.""",
        'title': 'Latest rocking chairs',
        'image': rocking_chairs[0].pictures.first().picture.url,
        # Page content
        'rocking_chairs': paged_rocking_chairs,
        'paginator': paginator,
    }, RequestContext(request))
    if request.is_ajax():
        return JsonResponse({
            'rocking_chairs': html,
            'current_page': page,
            'next_page': paged_rocking_chairs.next_page_number() if paged_rocking_chairs.has_next() else None,
            'previous_page': paged_rocking_chairs.previous_page_number() if paged_rocking_chairs.has_previous() else None
        })

    return HttpResponse(html)


def index_by_year(request):
    rocking_chairs = RockingChair.objects.published().order_by('year', 'name')
    return render(request, 'rocking_chair/index_by_year.html.jinja2', {
        # SEM metas
        'title': 'The great rocking chair time line',
        'description': """A complete time line of all rocking chairs ever designed, from the very first one to the latest
        additions to this ever-growing family""",
        'image': static('ftatr/images/rocking-chair-icon-540x540.png'),
        # Page content
        'timeline': build_index_by_year(rocking_chairs),
    })


def index_by_name(request):
    rocking_chairs = RockingChair.objects.published().order_by('name')
    return render(request, 'rocking_chair/index_by_name.html.jinja2', {
        # SEM metas
        'title': 'Rocking chairs ordered alphabetically',
        'description': """A list of all rocking chairs ever built each with pictures, designers' name and
        manufacturer's name, alphabetically ordered""",
        'image': static('ftatr/images/rocking-chair-icon-540x540.png'),
        # Page content
        'alphabet': build_index_by_name(rocking_chairs),
    })


def show(request, slug):
    rocking_chair = get_object_or_404(RockingChair, slug=slug)
    return render(request, 'rocking_chair/show.html.jinja2', {
        # SEM metas
        'title': '{rocking_chair} (rocking chair)'.format(rocking_chair=str(rocking_chair)),
        'description': """A list of all rocking chairs ever built each with pictures, designers' name and
        manufacturer's name, alphabetically ordered""",
        'image': static('ftatr/images/rocking-chair-icon-540x540.png'),
        # Page content
        'rocking_chair': rocking_chair,
    })
