from django.contrib.sites.models import Site
from django_jinja import library


@library.filter()
def absolute(relative_url):
    return 'http://%s%s' % (Site.objects.get_current().domain, relative_url)
