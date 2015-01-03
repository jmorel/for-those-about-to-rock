import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from rocking_chair.models import RockingChair


def index(request):
    # prepare general request
    rocking_chairs = RockingChair.objects \
        .exclude(published_at__gte=datetime.datetime.now()) \
        .exclude(published_at=None) \
        .order_by('-published_at')
    # set up paginator
    paginator = Paginator(rocking_chairs, 10)
    page = request.GET.get('page')
    try:
        paged_rocking_chairs = paginator.page(page)
    except PageNotAnInteger:
        paged_rocking_chairs = paginator.page(1)
    except EmptyPage:
        paged_rocking_chairs = paginator.page(paginator.num_pages)

    return render(request, 'rocking_chair/index.html.jinja2', {
        'rocking_chairs': paged_rocking_chairs,
        'paginator': paginator
    })


def show(request, slug):
    rocking_chair = get_object_or_404(RockingChair, slug=slug)
    return render(request, 'rocking_chair/show.html.jinja2', {
        'rocking_chair': rocking_chair,
        })