from django.contrib import admin
from for_those_about_to_rock.models import RockingChair, Designer, Year


class YearInline(admin.StackedInline):
    model = Year


class DesignerInline(admin.StackedInline):
    model = Designer.rocking_chairs.through
    extra = 1


class RockingChairAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        # ('Designer(s)', {'fields': })
    ]
    inlines = [YearInline, DesignerInline]
    list_display = ('name', )


class DesignerAdmin(admin.ModelAdmin):
    pass

admin.site.register(RockingChair, RockingChairAdmin)
admin.site.register(Designer, DesignerAdmin)
