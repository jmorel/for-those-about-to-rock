from django.shortcuts import render
from ftatr.models import RockingChair


def index(request):
    # todo : perform right query
    rocking_chairs = RockingChair.objects.all()

    context = {
        'rocking_chairs': rocking_chairs
    }
    return render(request, 'ftatr/index.html.jinja2', context)
