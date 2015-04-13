import datetime
from django.db.models import Count
from django.shortcuts import render
import simplejson
from anthology.models import RockingChair, Country, Designer, Manufacturer


def index(request):
    return render(request, 'analytics/index.html.jinja2', {
        'countries': simplejson.dumps(countries_serie()),
        'top_designers': simplejson.dumps(designers_serie()),
        'top_manufacturers': simplejson.dumps(manufacturers_serie()),
    })


def countries_serie():
    countries = {}

    designers = Designer.objects \
        .exclude(rocking_chairs__published_at__gte=datetime.datetime.now()) \
        .exclude(rocking_chairs__published_at=None)
    for designer in designers.all():
        for country in designer.nationalities.all():
            increment_serie(serie=countries, key=country.code, field='designers')

    manufacturers = Manufacturer.objects \
        .exclude(rocking_chairs__published_at__gte=datetime.datetime.now()) \
        .exclude(rocking_chairs__published_at=None)
    for manufacturer in manufacturers.all():
        increment_serie(serie=countries, key=manufacturer.country.code, field='manufacturers')

    rocking_chairs = RockingChair.objects \
        .exclude(published_at__gte=datetime.datetime.now()) \
        .exclude(published_at=None) \
        .order_by('-published_at')
    for rocking_chair in rocking_chairs.all():
        c1 = designers_countries(rocking_chair.designers.all())
        c2 = manufacturers_countries(rocking_chair.manufacturers.all())
        c = c1 + c2
        for country in c:
            increment_serie(serie=countries, key=country.code, field='rocking_chairs')

    serie = [{'name': code,
              'x': country['designers'],
              'y': country['manufacturers'],
              'z': country['rocking_chairs']} for code, country in countries.items()]

    return serie


def designers_countries(designers):
    countries = []
    for designer in designers:
        countries += designer.nationalities.all()
    return countries


def manufacturers_countries(manufacturers):
    return list(set([manufacturer.country for manufacturer in manufacturers]))


def increment_serie(serie, key, field, fields=('rocking_chairs', 'designers', 'manufacturers')):
    if key not in serie:
        serie[key] = {f: 0 for f in fields}
    serie[key][field] += 1


def designers_serie():
    designers = Designer.objects \
        .annotate(num_rocking_chairs=Count('rocking_chairs')) \
        .exclude(rocking_chairs__published_at__gte=datetime.datetime.now()) \
        .exclude(rocking_chairs__published_at=None) \
        .exclude(num_rocking_chairs__lte=1) \
        .order_by('-num_rocking_chairs')
    serie = [[designer.full_name, designer.num_rocking_chairs] for designer in designers[:20]]
    return serie


def manufacturers_serie():
    manufacturers = Manufacturer.objects \
        .annotate(num_rocking_chairs=Count('rocking_chairs')) \
        .exclude(rocking_chairs__published_at__gte=datetime.datetime.now()) \
        .exclude(rocking_chairs__published_at=None) \
        .exclude(num_rocking_chairs__lte=1) \
        .order_by('-num_rocking_chairs')
    serie = [[manufacturer.name, manufacturer.num_rocking_chairs] for manufacturer in manufacturers[:20]]
    return serie
