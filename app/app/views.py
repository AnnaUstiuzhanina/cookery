from django.shortcuts import render
from cookery.models import Ingredient


def index(request):
    ingredients = Ingredient.objects.all()
    return render(
        request,
        'recipes/index.html',
        {'ingredients': ingredients},
    )