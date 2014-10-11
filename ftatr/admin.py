from django.contrib import admin
from ftatr.models import RockingChair, Designer, Manufacturer, Picture, Price, DesignerLink, ManufacturerLink, YearLink, \
    Link, Currency, PriceLink


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
        PriceLinkInline,
        LinkInline,
        DesignerLinkInline,
        ManufacturerLinkInline,
        YearLinkInline,
    ]


class DesignerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'last_name', )}


class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(RockingChair, RockingChairAdmin)
admin.site.register(Designer, DesignerAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Picture)
admin.site.register(Currency)
