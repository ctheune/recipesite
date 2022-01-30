from django.db import models


class Recipe(models.Model):

    title = models.CharField("Titel", max_length=200)

    note = models.CharField("Notiz", max_length=200, null=True, blank=True)
    source = models.CharField("Quelle", max_length=200, null=True, blank=True)
    source_url = models.URLField("Quelle (URL)", null=True, blank=True)

    def __str__(self):
        return f'{self.id} – {self.title}'


class IngredientUsage(models.Model):

    recipe = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE, related_name='ingredients')

    amount = models.CharField('Menge', null=True, blank=True, max_length=30)
    unit = models.CharField('Einheit', null=True, blank=True, max_length=30)

    ingredient = models.ForeignKey('Ingredient', models.PROTECT)

    def __str__(self):
        return ' '.join(filter(bool, [self.amount, self.unit, str(self.ingredient)]))

    @classmethod
    def from_shortcut(cls, recipe, shortcut):
        parts = shortcut.split(' ', 2)
        if len(parts) == 1:
            amount = None
            unit = None
            ingredient = parts[0]
        elif len(parts) == 2:
            amount = parts[0]
            unit = None
            ingredient = parts[1]
        else:
            amount, unit, ingredient = parts

        if unit is None:
            unit = ''

        ing_obj, _ = Ingredient.objects.get_or_create(description=ingredient)

        print(recipe, amount, unit, ing_obj)
        usage = IngredientUsage.objects.create(
            recipe=recipe, amount=amount, unit=unit, ingredient=ing_obj)
        usage.save()


class Ingredient(models.Model):

    description = models.CharField('Zutat', max_length=200)

    def __str__(self):
        return self.description

    # calories / 100g after cooking
    # before/after cooking weight ratio
    # bad carbohydrates vs. good carbohydrates?
    # meat?
