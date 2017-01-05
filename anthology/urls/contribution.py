from django.conf.urls import url
from anthology.views import contribution

urlpatterns = [
    url(r'^$', contribution.index, name='index'),
]
