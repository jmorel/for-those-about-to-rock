import datetime
from optparse import make_option
from django.core.management import BaseCommand
from ftatr.settings import TWITTER_TOKEN, TWITTER_TOKEN_SECRET, TWITTER_CONSUMER_SECRET, TWITTER_CONSUMER_KEY
from anthology.models import RockingChair
from twitter import Twitter, OAuth, TwitterHTTPError


class Command(BaseCommand):
    help = 'Post today\'s rocking chair to twitter.'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--now',
                            dest='now',
                            action="store",
                            type=str,
                            help='Run assuming now is the specified datetime (format: 2014-04-21 27:03)'),
        parser.add_argument('--dry-run',
                            dest='dry-run',
                            action='store_true',
                            help='Dry-run: only display tweets, do not post them.'),

    def handle(self, *args, **options):
        now = datetime.datetime.now()
        if options['now']:
            try:
                now = datetime.datetime.strptime(options['now'], '%Y-%m-%d %H:%M')
            except ValueError:
                self.stdout.write('"{}" is an invalid datetime'.format(options['now']))
                return

        rocking_chairs = RockingChair.objects.filter(published_at__year=now.year,
                                                     published_at__month=now.month,
                                                     published_at__day=now.day,
                                                     published_at__lte=now)
        if not rocking_chairs:
            self.stdout.write('No rocking chair found for today ({})'.format(now))
            return

        t = Twitter(auth=OAuth(TWITTER_TOKEN, TWITTER_TOKEN_SECRET, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET))
        # compute current maximum text length for a tweet containing a link
        link_length = t.help.configuration()['short_url_length']
        tweet_max_length = 140 - link_length - 1
        for rocking_chair in rocking_chairs:
            tweet = rocking_chair.twitter_text(tweet_max_length=tweet_max_length)
            self.stdout.write('Found rocking chair: {}'.format(tweet))
            if options['dry-run']:
                self.stdout.write('Not posting (dry-run)')
                continue
            try:
                t.statuses.update(status=tweet)
            except TwitterHTTPError:
                self.stdout.write('Tweet already posted')
