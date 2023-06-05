from django.db import models
from django.utils.formats import localize


class Week(models.Model):
    """A week aggregates multiple days that we use as one "unit" of
    planning for creating a printed weekly plan, shopping lists, etc.

    """

    class Meta:
        verbose_name = "Woche"
        verbose_name_plural = "Wochen"

    def __str__(self):
        start = localize(self.first.day, use_l10n=True)
        end = localize(self.last.day, use_l10n=True)
        return f"Woche vom {start} bis {end}"

    @property
    def first(self):
        return list(sorted(self.days.all(), key=lambda x: x.day))[0]

    @property
    def last(self):
        return list(sorted(self.days.all(), key=lambda x: x.day))[-1]

    @classmethod
    def generate_next_week(self):
        pass


class Day(models.Model):
    """What is planned for a single day.

    For now this includes which recipe to eat for dinner and
    a field for manual annotations of special events.
    """

    week = models.ForeignKey("Week", on_delete=models.CASCADE, related_name="days")

    day = models.DateField("Datum")

    dinner = models.ForeignKey(
        "recipedb.Recipe", on_delete=models.SET_NULL, blank=True, null=True
    )

    dinner_freestyle = models.CharField(
        "Dinner (alternativ)", max_length=200, null=True, blank=True
    )

    note = models.CharField("Notiz", max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["day"]

    def __str__(self):
        return f"Tag {self.day}"
