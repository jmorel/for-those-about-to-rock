import datetime
from django.contrib.sitemaps import Sitemap
from rocking_chair.models import RockingChair


class FTATRSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return RockingChair.objects \
            .exclude(published_at__gte=datetime.datetime.now()) \
            .exclude(published_at=None) \
            .order_by('-published_at')

    def lastmod(self, obj):
        return obj.updated_at
