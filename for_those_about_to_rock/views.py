from django.shortcuts import render
from for_those_about_to_rock.models import RockingChair


def index(request):
    # todo : perform right query
    rocking_chairs = RockingChair.objects.all()

    context = {
        'rocking_chairs': rocking_chairs
    }
    return render(request, 'for_those_about_to_rock/index.html.jinja2', context)
