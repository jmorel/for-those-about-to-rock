import datetime
from django.contrib.sites.models import Site
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse
from django.db import models
import hashlib
import os
from anthology.managers import DesignerManager, ManufacturerManager, RockingChairManager


class RockingChair(models.Model):
    class Meta:
        db_table = 'rocking_chair'

    objects = RockingChairManager()

    name = models.CharField(max_length=255)
    year = models.IntegerField(max_length=4, null=True, blank=True)

    # price = models.OneToOneField('Price', blank=True, null=True)
    designers = models.ManyToManyField('Designer', related_name='rocking_chairs', blank=True)
    manufacturers = models.ManyToManyField('Manufacturer', related_name='rocking_chairs', blank=True)

    slug = models.SlugField(unique=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_published(self):
        return self.published_at and (self.published_at < datetime.datetime.now())

    def get_absolute_url(self):
        return reverse('rocking_chair:show', kwargs={'slug': self.slug})

    def twitter_text(self, tweet_max_length=118):
        # rocking chair name
        safe_tweet = self.name
        if len(safe_tweet) > tweet_max_length:
            safe_tweet = safe_tweet[:tweet_max_length - 3] + '...'
        # add designer names
        if self.designer_names:
            tweet = "{} by {}".format(safe_tweet, self.designer_names)
            if len(tweet) <= tweet_max_length:
                safe_tweet = tweet
        # add manufacturer names
        if self.manufacturer_names:
            tweet = "{} ({})".format(safe_tweet, self.manufacturer_names)
            if len(tweet) <= tweet_max_length:
                safe_tweet = tweet
        return "{} {}{}".format(safe_tweet, Site.objects.get_current(), self.get_absolute_url())

    @property
    def title(self):
        return self.build_title()

    def build_title(self, designers=True, manufacturers=True):
        title = self.name
        if designers and self.designer_names:
            title = "{} by {}".format(title, self.designer_names)
        if manufacturers and self.manufacturer_names:
            title = "{} ({})".format(title, self.manufacturer_names)
        return title

    @property
    def designer_names(self):
        designers = list(self.designers.all())
        if not designers:
            return None

        authors = ', '.join([designer.full_name for designer in designers[:-1]])
        if authors:
            authors = "{} and {}".format(authors, designers[-1].full_name)
        else:
            authors = designers[-1].full_name
        return authors

    @property
    def manufacturer_names(self):
        manufacturers = list(self.manufacturers.all())
        if not manufacturers:
            return None

        names = ', '.join(map(lambda manufacturer: manufacturer.name, manufacturers))
        return names

    def get_upload_to(self, filename):
        return os.path.join('rocking-chairs', self.rocking_chair.slug, get_upload_filename(filename))

    @property
    def contribution_type(self):
        return Contribution.TYPE_ROCKING_CHAIR


def get_upload_filename(filename):
    name, extension = os.path.splitext(filename)
    md5sum = hashlib.md5()
    md5sum.update(filename.encode('utf-8'))
    md5sum.update(str(datetime.datetime.now()).encode('utf-8'))
    md5sum = md5sum.hexdigest()
    return md5sum + extension


class Picture(models.Model):
    class Meta:
        db_table = 'picture'
        ordering = ['priority', ]

    picture = models.ImageField(upload_to=RockingChair.get_upload_to)
    priority = models.SmallIntegerField(null=True, blank=True)

    rocking_chair = models.ForeignKey('RockingChair', related_name='pictures')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class Price(models.Model):
    class Meta:
        db_table = 'price'

    amount = models.FloatField()

    rocking_chair = models.OneToOneField('RockingChair', related_name='price', blank=True, null=True)
    currency = models.ForeignKey('Currency')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.amount, self.currency.code)


class Designer(models.Model):
    class Meta:
        db_table = 'designer'

    def get_upload_to(self, filename):
        return os.path.join('designers', self.slug, get_upload_filename(filename))

    objects = DesignerManager()

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)

    portrait = models.ImageField(upload_to=get_upload_to, blank=True, null=True)

    nationalities = models.ManyToManyField('Country', blank=True)

    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name).strip()

    @property
    def published_rocking_chairs(self):
        return self.rocking_chairs.filter(published_at__lte=datetime.datetime.now())

    def get_absolute_url(self):
        return reverse('designer:show', kwargs={'slug': self.slug})


class Manufacturer(models.Model):
    class Meta:
        db_table = 'manufacturer'

    def get_upload_to(self, filename):
        return os.path.join('manufacturers', self.slug, get_upload_filename(filename))

    objects = ManufacturerManager()

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=get_upload_to, blank=True, null=True)

    country = models.ForeignKey('Country', blank=True, null=True)

    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def published_rocking_chairs(self):
        return self.rocking_chairs.filter(published_at__lte=datetime.datetime.now())

    def get_absolute_url(self):
        return reverse('manufacturer:show', kwargs={'slug': self.slug})


class Link(models.Model):
    class Meta:
        db_table = 'rocking_chair_links'

    url = models.CharField(max_length=255)

    rocking_chair = models.ForeignKey('RockingChair', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class DesignerLink(models.Model):
    class Meta:
        db_table = 'designer_link'

    url = models.CharField(max_length=255)

    rocking_chair = models.ForeignKey('RockingChair', related_name='designer_links')
    designer = models.ForeignKey('Designer', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class ManufacturerLink(models.Model):
    class Meta:
        db_table = 'manufacturer_link'

    url = models.CharField(max_length=255)

    rocking_chair = models.ForeignKey('RockingChair', related_name='manufacturer_links')
    manufacturer = models.ForeignKey('Manufacturer', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class PriceLink(models.Model):
    class Meta:
        db_table = 'price_link'

    url = models.CharField(max_length=255)

    rocking_chair = models.ForeignKey('RockingChair', related_name='price_links')
    price = models.ForeignKey('Price', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class YearLink(models.Model):
    class Meta:
        db_table = 'year_link'

    url = models.CharField(max_length=255)

    rocking_chair = models.ForeignKey('RockingChair', related_name='year_links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class Currency(models.Model):
    class Meta:
        db_table = 'currency'
        verbose_name_plural = 'currencies'

    name = models.TextField()
    code = models.TextField()

    def __str__(self):
        return self.name


class Country(models.Model):
    class Meta:
        db_table = 'country'
        verbose_name_plural = 'countries'

    name = models.TextField()
    code = models.TextField()

    def __str__(self):
        return self.name


class Contribution(models.Model):
    TYPE_ROCKING_CHAIR = 'rocking_chair'
    TYPE_DESIGNER = 'designer'
    TYPE_MANUFACTURER = 'manufacturer'

    TARGET_TYPES = (
        (TYPE_ROCKING_CHAIR, 'Rocking chair'),
        (TYPE_DESIGNER, 'Designer'),
        (TYPE_MANUFACTURER, 'Manufacturer')
    )

    STATUS_NEW = 'new'
    STATUS_CLOSED = 'closed'
    STATUSES = (
        (STATUS_NEW, 'New'),
        (STATUS_CLOSED, 'Closed'),
    )
    sender = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    target_type = models.CharField(max_length=15, blank=False, null=False, choices=TARGET_TYPES, editable=False)
    target_slug = models.CharField(max_length=100, blank=False, null=False, editable=False)

    status = models.CharField(max_length=10, blank=False, null=False, default=STATUS_NEW, choices=STATUSES)

    created_at = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return "From {sender} on {created_at}".format(sender=self.sender,
                                                      created_at=self.created_at.isoformat())

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        super().save(*args, **kwargs)

    @property
    def email_subject(self):
        return "New contribution for {type} \"{name}\"".format(type=self.target_type,
                                                               name=str(self.related_model))

    @property
    def related_model(self):
        if self.target_type == Contribution.TYPE_ROCKING_CHAIR:
            return RockingChair.objects.get(slug=self.target_slug)
        if self.target_type == Contribution.TYPE_DESIGNER:
            return Designer.objects.get(slug=self.target_slug)
        if self.target_type == Contribution.TYPE_MANUFACTURER:
            return Manufacturer.objects.get(slug=self.target_slug)

    @property
    def email_message(self):
        return """
New contribution for {type} "{name}"
Contribution created on {created_at}


Sender: {sender}
Message:
{message}""".format(type=self.target_type,
                    name=str(self.related_model),
                    created_at=str(self.created_at),
                    sender=self.sender,
                    message=self.message)

    def send_notification(self):
        mail_admins(subject=self.email_subject,
                    message=self.email_message)
