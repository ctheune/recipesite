# Generated by Django 4.0.1 on 2022-01-17 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ingredient",
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
                ("description", models.CharField(max_length=200, verbose_name="Zutat")),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
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
                ("title", models.CharField(max_length=200, verbose_name="Titel")),
                (
                    "note",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Notiz"
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Quelle"
                    ),
                ),
                (
                    "source_url",
                    models.URLField(blank=True, null=True, verbose_name="Quelle (URL)"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IngredientUsage",
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
                (
                    "amount",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Menge"
                    ),
                ),
                (
                    "unit",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Einheit"
                    ),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="recipedb.ingredient",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ingredients",
                        to="recipedb.recipe",
                    ),
                ),
            ],
        ),
    ]
