# Generated by Django 4.0.1 on 2022-02-05 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("recipedb", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Week",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Day",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day", models.DateField(verbose_name="Datum")),
                (
                    "note",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Notiz"
                    ),
                ),
                (
                    "dinner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="recipedb.recipe",
                    ),
                ),
                (
                    "week",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="days",
                        to="weekplanner.week",
                    ),
                ),
            ],
        ),
    ]
