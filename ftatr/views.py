# django
from django.shortcuts import render
from django.templatetags.static import static

# ftatr
from anthology.models import RockingChair
from ftatr.forms import ContactMessageForm
from ftatr.utils import is_recaptcha_valid


def about(request):
    return render(request, 'about.html.jinja2', {
        # SEM metas
        'title': 'About this anthology',
        'description': """Everything there is to know about this anthology.""",
        'image': static('ftatr/images/rocking-chair-icon-540x540.png'),
        # Page content
        'mt3': RockingChair.objects.get(slug='mt3'),
        'spun': RockingChair.objects.get(slug='spun'),
        'sol': RockingChair.objects.get(slug='sol'),
        'cradle': RockingChair.objects.get(slug='cradle'),
        'sway': RockingChair.objects.get(slug='sway'),
        'hummingbird': RockingChair.objects.get(slug='humingbird'),
        'gravity_balans': RockingChair.objects.get(slug='gravity-balans'),
        'thatsit': RockingChair.objects.get(slug='thatsit'),
    })


def contact(request):
    is_recaptcha_valid_result = None
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        is_recaptcha_valid_result = is_recaptcha_valid(request)
        if form.is_valid() and is_recaptcha_valid_result:
            contact_message = form.save()
            contact_message.send()
            return render(request, 'contact_success.html.jinja2', {
                # SEM metas
                'title': 'Contact the authors',
                'description': """Contact the authors of this anthology through either plain old email, twitter or the provided
                form.""",
                'image': static('ftatr/images/rocking-chair-icon-540x540.png'),
            })
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html.jinja2', {
        # SEM metas
        'title': 'Contact the authors',
        'description': """Contact the authors of this anthology through either plain old email, twitter or the provided
        form.""",
        'image': static('ftatr/images/rocking-chair-icon-540x540.png'),
        # Page content
        'form': form,
        'is_recaptcha_valid': is_recaptcha_valid_result
    })
