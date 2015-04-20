from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.template.loader import render_to_string, get_template
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

    template = get_template('rocking_chair/index.html.jinja2')
    html = template.render(Context({'rocking_chairs': paged_rocking_chairs,
                                    'paginator': paginator,
                                    'request': request}))
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
        'timeline': build_index_by_year(rocking_chairs),
    })


def index_by_name(request):
    rocking_chairs = RockingChair.objects.published().order_by('name')
    return render(request, 'rocking_chair/index_by_name.html.jinja2', {
        'alphabet': build_index_by_name(rocking_chairs),
    })


def show(request, slug):
    rocking_chair = get_object_or_404(RockingChair, slug=slug)
    return render(request, 'rocking_chair/show.html.jinja2', {
        'rocking_chair': rocking_chair,
    })
