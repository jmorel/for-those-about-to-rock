from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin
from contribution.models import Contribution, Source


class SourceInline(TabularInline):
    model = Source
    extra = 1


class ContributionAdmin(ModelAdmin):
    inlines = [SourceInline, ]
    list_display = ('status', '__str__', )
    list_filter = ('status', )

admin.site.register(Contribution, ContributionAdmin)
admin.site.register(Source)
