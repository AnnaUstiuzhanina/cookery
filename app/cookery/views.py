from rest_framework import viewsets
from .models import Ingredient, Recipe, RecipeIngredient
from .serializers import IngredientSerializer, RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        name = self.request.query_params.get('name')

        if name is not None:
            queryset = queryset.filter(name__contains=name)

        ingredients = self.request.query_params.get('ingredients')

        if ingredients:
            print(ingredients.split(','))

            recipe_ingredients = RecipeIngredient.objects.filter(
                ingredient__id__in=ingredients.split(','),
            )

            recipe_ids = [ring['recipe__id'] for ring in recipe_ingredients.values('recipe__id')]
            queryset = queryset.filter(id__in=recipe_ids)

        return queryset
