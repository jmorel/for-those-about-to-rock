from django.contrib import admin
from ftatr.models import RockingChair, Designer, Manufacturer, Picture, Price, DesignerLink, ManufacturerLink, YearLink, \
    Link, Currency


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


class RockingChairAdmin(admin.ModelAdmin):
    inlines = [LinkInline, PictureInline, DesignerLinkInline, ManufacturerLinkInline, YearLinkInline]


admin.site.register(RockingChair, RockingChairAdmin)
admin.site.register(Designer)
admin.site.register(Manufacturer)
admin.site.register(Picture)
admin.site.register(Currency)
