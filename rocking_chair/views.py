from collections import OrderedDict
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


def index_by_year(request):
    # prepare general request
    rocking_chairs = RockingChair.objects \
        .exclude(published_at__gte=datetime.datetime.now()) \
        .exclude(published_at=None) \
        .order_by('year', 'name')
    # index by years
    timeline = OrderedDict()
    current_year = datetime.datetime.now().year
    for year in reversed(range(rocking_chairs[0].year, current_year + 1)):
        timeline[year] = []
    for rocking_chair in rocking_chairs:
        timeline[rocking_chair.year].append(rocking_chair)
    return render(request, 'rocking_chair/index_by_year.html.jinja2', {
        'timeline': timeline,
    })


def index_by_name(request):
    # prepare general request
    rocking_chairs = RockingChair.objects \
        .exclude(published_at__gte=datetime.datetime.now()) \
        .exclude(published_at=None) \
        .order_by('name')
    # index by name
    alphabet = OrderedDict()
    for letter in 'abcdefghijklmnopqrstuvwxyz#':
        alphabet[letter] = []
    for rocking_chair in rocking_chairs:
        letter = rocking_chair.name.lower()[0]
        letter = letter if letter in 'abcdefghijklmnopqrstuvwxyz' else '#'
        alphabet[letter].append(rocking_chair)
    return render(request, 'rocking_chair/index_by_name.html.jinja2', {
        'alphabet': alphabet,
    })


def show(request, slug):
    rocking_chair = get_object_or_404(RockingChair, slug=slug)
    return render(request, 'rocking_chair/show.html.jinja2', {
        'rocking_chair': rocking_chair,
    })
