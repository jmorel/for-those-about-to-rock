from django.conf.urls import patterns, url
from rocking_chair import views, feeds

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^feed$', feeds.LatestRockingChairsFeed(), name='feed'),
    url(r'^(?P<slug>\w+)$', views.show, name='show'),
)
