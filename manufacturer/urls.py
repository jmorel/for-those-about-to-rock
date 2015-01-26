from django.conf.urls import patterns, url
from manufacturer import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index_by_name, name='index-by-name'),
    url(r'^/by-country$', views.index_by_country, name='index-by-country'),
    url(r'^(?P<slug>[-\w]+)$', views.show, name='show'),
)
