from django.conf.urls import patterns, url
from manufacturer import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[-\w]+)$', views.show, name='show'),
)
