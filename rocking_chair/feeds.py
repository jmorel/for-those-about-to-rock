import datetime
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from rocking_chair.models import RockingChair


class LatestRockingChairsFeed(Feed):
    title = 'For Those About To Rock : latest rocking chairs'
    link = '/feed'
    description = 'Latest rocking chairs published on For Those About To Rock'

    def items(self):
        rocking_chairs = RockingChair.objects \
            .exclude(published_at__gte=datetime.datetime.now()) \
            .exclude(published_at=None) \
            .order_by('-published_at')[:10]
        return rocking_chairs

    def item_title(self, item):
        return item.twitter_text

    def item_description(self, item):
        return item.twitter_text

    def item_link(self, item):
        return reverse('rocking_chair:show', args={'slug': item.slug})

