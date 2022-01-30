from django.contrib import admin


from .models import Recipe, Ingredient, IngredientUsage


class IngredientUsageInline(admin.StackedInline):
    model = IngredientUsage
    extra = 3


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientUsageInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
