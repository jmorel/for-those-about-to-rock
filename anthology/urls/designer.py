from django.conf.urls import url
from anthology.views import designer

urlpatterns = [
    url(r'^$', designer.index, name='index'),
    url(r'^(?P<slug>[-\w]+)$', designer.show, name='show'),
]
