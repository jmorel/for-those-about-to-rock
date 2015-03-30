from django.conf.urls import patterns, url
from anthology.views import analytics

urlpatterns = patterns(
    '',
    url(r'^$', analytics.index, name='index'),
)
