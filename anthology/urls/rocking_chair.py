from django.conf.urls import url
from anthology import feeds
from anthology.views import rocking_chair

urlpatterns = [
    url(r'^$', rocking_chair.index, name='index'),
    url(r'^by-name$', rocking_chair.index_by_name, name='index-by-name'),
    url(r'^by-year$', rocking_chair.index_by_year, name='index-by-year'),
    url(r'^feed$', feeds.LatestRockingChairsFeed(), name='feed'),
    url(r'^(?P<slug>[-\w]+)$', rocking_chair.show, name='show'),
]
