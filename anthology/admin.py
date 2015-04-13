from collections import OrderedDict
import datetime
from django.conf.urls import patterns, url
from django.contrib import admin
from django.shortcuts import render
from anthology.models import RockingChair, Designer, Manufacturer, Picture, Price, DesignerLink, ManufacturerLink, \
    YearLink, Link, Currency, PriceLink, Country


class DesignerLinkInline(admin.TabularInline):
    model = DesignerLink
    extra = 1


class ManufacturerLinkInline(admin.TabularInline):
    model = ManufacturerLink
    extra = 1


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


class YearLinkInline(admin.TabularInline):
    model = YearLink
    extra = 1


class PictureInline(admin.TabularInline):
    model = Picture
    extra = 1


class PriceInline(admin.TabularInline):
    model = Price


class PriceLinkInline(admin.TabularInline):
    model = PriceLink
    extra = 1


class RockingChairAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    inlines = [
        PictureInline,
        PriceInline,
        LinkInline,
        PriceLinkInline,
        DesignerLinkInline,
        ManufacturerLinkInline,
        YearLinkInline,
    ]
    search_fields = ('name', 'designers__first_name', 'designers__last_name', 'manufacturers__name')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = patterns(
            '',
            url(r'^timeline/$', self.admin_site.admin_view(self.timeline_view), name='rocking_chair_timeline')
        )
        return custom_urls + urls

    def timeline_view(self, request):
        unscheduled = RockingChair.objects \
            .filter(published_at=None)
        scheduled = RockingChair.objects \
            .exclude(published_at=None) \
            .order_by('-published_at')
        # Build timeline
        timeline = OrderedDict()
        today = datetime.date.today()
        if scheduled:
            date = max(today, scheduled.first().published_at.date())
            min_date = min(today, scheduled.last().published_at.date())
            while date >= min_date:
                timeline[date] = []
                date = date - datetime.timedelta(days=1)

            for rocking_chair in scheduled:
                day = rocking_chair.published_at.date()
                timeline[day].append(rocking_chair)

        return render(request, 'admin/anthology/timeline.html', {
            'unscheduled': unscheduled,
            'timeline': timeline,
            'opts': self.opts,
            'title': 'Rocking-chair publishing timeline',
            'today': today
        })


class DesignerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'last_name', )}
    ordering = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    ordering = ('name', )
    search_fields = ('name', )


admin.site.register(RockingChair, RockingChairAdmin)
admin.site.register(Designer, DesignerAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Picture)
admin.site.register(Currency)
admin.site.register(Country)
