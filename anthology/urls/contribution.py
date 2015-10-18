from django.conf.urls import patterns, url
from anthology.views import contribution

urlpatterns = patterns(
    '',
    url(r'^$', contribution.index, name='index'),
)
