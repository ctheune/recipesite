from django.urls import path

from . import views

app_name = "weekplanner"
urlpatterns = [
    path("", views.WeeksView.as_view(), name="index"),
    path("<int:week>", views.SingleWeekView.as_view(), name="week"),
]
