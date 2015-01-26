from collections import OrderedDict
from django.shortcuts import render, get_object_or_404
from rocking_chair.models import Manufacturer


def show(request, slug):
    manufacturer = get_object_or_404(Manufacturer, slug=slug)
    return render(request, 'manufacturer/show.html.jinja2', {
        'manufacturer': manufacturer
    })


def index_by_name(request):
    manufacturers = Manufacturer.objects.order_by('name')
    alphabet = OrderedDict()
    for letter in 'abcdefghijkhmnopqrstuvwxyz':
        alphabet[letter] = []
    for manufacturer in manufacturers:
        alphabet[manufacturer.name[0]].append(manufacturer)

    return render(request, 'manufacturer/index_by_name.html.jinja2', {
        'alphabet': alphabet
    })


def index_by_country(request):
    manufacturers = Manufacturer.objects.order_by('country__name, name')
    countries = {}
    for manufacturer in manufacturers:
        if manufacturer.country.name not in countries:
            countries[manufacturer.country.name] = []
        countries[manufacturer.country.name].append(manufacturer)

    return render(request, 'manufacturer/index_by_country.html.jinja2', {
        'countries': countries
    })
