from django.conf.urls import patterns, url
from anthology.views import designer

urlpatterns = patterns(
    '',
    url(r'^$', designer.index, name='index'),
    url(r'^(?P<slug>[-\w]+)$', designer.show, name='show'),
)
