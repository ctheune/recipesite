from datetime import timedelta

from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from recipedb.models import recipe_for_day

from .models import Day, Week

DAY = timedelta(days=1)


class DayFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(DayFormSet, self).__init__(*args, **kwargs)

        last_day = Day.objects.latest("day").day

        self.initial = [
            {
                "day": str(last_day + x * DAY),
                "dinner": recipe_for_day(last_day + x * DAY),
            }
            for x in range(1, 8)
        ]


class DayInline(admin.StackedInline):
    model = Day
    extra = 7
    formset = DayFormSet


class WeekAdmin(admin.ModelAdmin):
    inlines = [DayInline]

    search_fields = ["question_text"]

    list_display = ("first_day", "last_day")

    @admin.display(description="First day")
    def first_day(self, obj):
        return obj.first.day

    @admin.display(description="Last day")
    def last_day(self, obj):
        return obj.last.day


class DayAdmin(admin.ModelAdmin):
    autocomplete_fields = ["dinner"]

    def get_model_perms(self, request):
        # This is a hack to not get the 'Days' entry in the admin sidebar menu
        return {}


admin.site.register(Day, DayAdmin)
admin.site.register(Week, WeekAdmin)
