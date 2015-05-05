from django.conf.urls import patterns, url
from contribution.views import new, success

urlpatterns = patterns(
    '',
    url(r'^new$', new, name='new'),
    url(r'^success$', success, name='success'),
)
