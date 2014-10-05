from django.contrib import admin
from ftatr.models import RockingChair, Designer, Year, Manufacturer, Picture


# class YearInline(admin.StackedInline):
#     model = Year
#
#
# class PictureInline(admin.TabularInline):
#     model = Picture
#     extra = 1
#
#
# class DesignerInline(admin.TabularInline):
#     model = Designer.rocking_chairs.through
#     exclude = ('rocking_chairs', )
#     extra = 1
#
#
# class ManufacturerInline(admin.TabularInline):
#     model = Manufacturer.rocking_chairs.through
#     extra = 1
#
#
# class RockingChairAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields': ['name']}), ]
#     inlines = [YearInline, PictureInline, DesignerInline, ManufacturerInline]


# admin.site.register(RockingChair, RockingChairAdmin)
admin.site.register(RockingChair)
admin.site.register(Designer)
admin.site.register(Manufacturer)
