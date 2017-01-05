from django.conf.urls import url
from anthology.views import manufacturer

urlpatterns = [
    url(r'^$', manufacturer.index, name='index'),
    url(r'^(?P<slug>[-\w]+)$', manufacturer.show, name='show'),
]
