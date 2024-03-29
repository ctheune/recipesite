from .models import Recipe, week_for_day, recipe_for_day
from django.views import generic
import datetime

DAY_MAPPING = {
    0: "Montag",
    1: "Dienstag",
    2: "Mittwoch",
    3: "Donnerstag",
    4: "Freitag",
    5: "Samstag",
    6: "Sonntag",
}


class IndexView(generic.TemplateView):
    """The "infinite menu"."""

    template_name = "recipes/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipes = list(Recipe.objects.order_by("id").all())

        context["current_week"] = current_week = week_for_day(datetime.date.today())
        context["weeks"] = []
        week = None
        day = 0
        while recipes:
            if not week:
                week = {"weeknumber": len(context["weeks"]) + 1, "days": []}
            week["is_current"] = week["weeknumber"] == current_week
            week["days"].append({"day": DAY_MAPPING[day], "recipe": recipes.pop(0)})
            day += 1
            if day == 7:
                context["weeks"].append(week)
                week = None
                day = 0
        return context
