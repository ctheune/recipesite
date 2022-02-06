from django.core.management.base import BaseCommand
from recipedb.models import Recipe, Ingredient, IngredientUsage
import json


class Command(BaseCommand):
    help = "Imports recipes from a JSON file."

    def add_arguments(self, parser):
        parser.add_argument("filename")

    def handle(self, *args, **options):
        # Delete existing objects
        Recipe.objects.all().delete()
        Ingredient.objects.all().delete()

        with open(options["filename"], "r") as f:
            import_recipes = json.load(f)

        self.stdout.write(f"Importing {len(import_recipes)}")

        for import_recipe in import_recipes:
            recipe = Recipe(
                id=import_recipe["id"],
                title=import_recipe["recipe"],
                source=import_recipe["source"],
                source_url=import_recipe.get("source_url"),
                note=import_recipe["note"],
            )
            recipe.save()
            for i in import_recipe["ingredients"]:
                IngredientUsage.from_shortcut(recipe, i)
