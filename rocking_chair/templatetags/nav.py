from django.shortcuts import render
from django.template.loader import render_to_string
from django_jinja import library
from haystack.forms import SearchForm


@library.global_function
def nav(active_page='rocking_chair:index', query=None, open=False):
    pages = [
        {
            'url': 'rocking_chair:index',
            'picture': 1,
            'caption': 'Last entries'
        },
        {
            'url': 'search',
            'picture': '<i class="fa fa-search"></i>',
            'caption': 'search'
        },
        {
            'url': 'rocking_chair:index-by-year',
            'picture': 2,
            'caption': 'Timeline'
        },
        {
            'url': 'rocking_chair:index-by-name',
            'picture': 2,
            'caption': 'Rocking chairs'
        },
        {
            'url': 'manufacturer:index',
            'picture': 2,
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
