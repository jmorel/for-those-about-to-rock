from django.conf.urls import url
from anthology.views import analytics

urlpatterns = [
    url(r'^$', analytics.index, name='index'),
]
