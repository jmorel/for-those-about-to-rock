from django.shortcuts import render
from django.template.loader import render_to_string
from django.templatetags.static import static
from django_jinja import library
from haystack.forms import SearchForm


@library.global_function
def nav(active_page='rocking_chair:index', query=None, open=False):
    pages = [
        {
            'url': 'rocking_chair:index',
            'picture': '<i class="fa fa-clock-o"></i>',
            'caption': 'Last entries'
        },
        {
            'url': 'search',
            'picture': '<i class="fa fa-search"></i>',
            'caption': 'search'
        },
        {
            'url': 'rocking_chair:index-by-year',
            'picture': '<img src="{}" alt="Timeline">'.format(
                static('ftatr/images/timeline-icon-50x50.png')),
            'caption': 'Timeline'
        },
        {
            'url': 'rocking_chair:index-by-name',
            'picture': '<img src="{}" alt="Rocking chairs">'.format(
                static('ftatr/images/rocking-chair-icon-50x50.png')),
            'caption': 'Rocking chairs'
        },
        {
            'url': 'manufacturer:index',
            'picture': '<img src="{}" alt="Manufacturers">'.format(
                static('ftatr/images/factory-icon-50x50.png')),
            'caption': 'Manufacturers'
        },
        {
            'url': 'designer:index',
            'picture': '<i class="fa fa-users"></i>',
            'caption': 'Manufacturers'
        },
    ]
    ordered_pages = []
    for page in pages:
        if page['url'] == active_page:
            i = pages.index(page)
            ordered_pages = pages[i:] + pages[:i]
    return render_to_string('nav.html.jinja2', {
        'items': ordered_pages or pages,
        'search_form': SearchForm(),
        'query': query,
        'open': open,
    })
