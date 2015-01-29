from django.shortcuts import render
from django.template.loader import render_to_string
from django_jinja import library


@library.global_function
def nav(active_page='rocking_chair:index'):
    pages = [
        {
            'url': 'rocking_chair:index',
            'picture': 1,
            'caption': 'Last entries'
        },
        {
            'url': 'search.html',
            'picture': '<i class="fa fa-search"></i>',
            'caption': 'search'
        },
        {
            'url': 'rocking_chair:index-by-year',
            'picture': 2,
            'caption': 'Rocking chairs by year'
        },
    ]
    ordered_pages = []
    for page in pages:
        if page['url'] == active_page:
            i = pages.index(page)
            ordered_pages = pages[i:] + pages[:i]
    return render_to_string('nav.html.jinja2', {
        'items': ordered_pages or pages
    })
