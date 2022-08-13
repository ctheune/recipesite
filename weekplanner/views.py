from .models import Week
from django.views import generic


class WeeksView(generic.TemplateView):
    """The week planner overview."""

    template_name = "weekplan/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["weeks"] = list(Week.objects.order_by("-id").all())
        return context


class SingleWeekView(generic.TemplateView):

    template_name = "weekplan/singleweek.html"

    def get_context_data(self, week, **kwargs):
        context = super().get_context_data(**kwargs)
        context["week"] = Week.objects.get(id=week)
        return context
