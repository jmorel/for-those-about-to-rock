from django.conf.urls import patterns, url
from rocking_chair import views, feeds

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^by-name$', views.index_by_name, name='index-by-name'),
    url(r'^by-year$', views.index_by_year, name='index-by-year'),
    url(r'^feed$', feeds.LatestRockingChairsFeed(), name='feed'),
    url(r'^(?P<slug>[-\w]+)$', views.show, name='show'),
)
