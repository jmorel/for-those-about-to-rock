from django.conf.urls import patterns, url
from rocking_chair.views import manufacturer

urlpatterns = patterns(
    '',
    url(r'^$', manufacturer.index, name='index'),
    url(r'^(?P<slug>[-\w]+)$', manufacturer.show, name='show'),
)
