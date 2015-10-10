from django.shortcuts import render
from django.templatetags.static import static

from ftatr.forms import ContactMessageForm


def about(request):
    return render(request, 'about.html.jinja2', {
        # SEM metas
        'title': 'About this anthology',
        'description': """Everything there is to know about this anthology.""",
        'image': static('ftatr/images/rocking-chair-icon-540x540.png'),
        # Page content
    })


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
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
    })
