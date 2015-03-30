from django.conf.urls import patterns, url
from rocking_chair.views import analytics

urlpatterns = patterns(
    '',
    url(r'^$', analytics.index, name='index'),
)
