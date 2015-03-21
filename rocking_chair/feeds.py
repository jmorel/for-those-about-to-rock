import datetime
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.template import loader
from django.utils.feedgenerator import Atom1Feed
from rocking_chair.models import RockingChair


class LatestRockingChairsFeed(Feed):
    feed_type = Atom1Feed
    title = 'For Those About To Rock : latest rocking chairs'
    description = 'Latest rocking chairs published on For Those About To Rock'
    author_name = 'Jérémy Morel'
    author_email = 'jeremy@forthoseabouttorock.io'
    author_link = 'http://forthoseabouttorock.io'
    icon = 'test'

    def link(self):
        return reverse('rocking_chair:feed')

    def feed_url(self):
        return reverse('rocking_chair:feed')

    def items(self):
        rocking_chairs = RockingChair.objects \
            .exclude(published_at__gte=datetime.datetime.now()) \
            .exclude(published_at=None) \
            .order_by('-published_at')[:10]
        return rocking_chairs

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        template = loader.get_template('rocking_chair/feed_item.html.jinja2')
        return template.render({'rocking_chair': item})

    def item_link(self, item):
        return reverse('rocking_chair:show', kwargs={'slug': item.slug})

    def item_pubdate(self, item):
        return item.published_at

    def item_updateddate(self, item):
        return item.updated_at

