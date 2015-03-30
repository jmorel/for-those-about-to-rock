from django.conf.urls import patterns, url
from rocking_chair import feeds
from rocking_chair.views import rocking_chair

urlpatterns = patterns(
    '',
    url(r'^$', rocking_chair.index, name='index'),
    url(r'^by-name$', rocking_chair.index_by_name, name='index-by-name'),
    url(r'^by-year$', rocking_chair.index_by_year, name='index-by-year'),
    url(r'^feed$', feeds.LatestRockingChairsFeed(), name='feed'),
    url(r'^(?P<slug>[-\w]+)$', rocking_chair.show, name='show'),
)
