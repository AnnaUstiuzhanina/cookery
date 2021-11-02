from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Recipe(models.Model):
    '''
    Модель рецепта:
    name - название рецепта
    description - описание рецепта
    ingredients - ингредиенты рецепта
    '''
    name = models.CharField(
        max_length=100,
        verbose_name='название рецепта',
    )
    description = models.TextField(
        max_length=254,
        verbose_name='описание рецепта',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Ingredient(models.Model):
    '''
    Модель ингредиента:
    name - название ингредиента
    measure_unit - единица измерения ингредиента
    '''

    name = models.CharField(
        max_length=200,
        verbose_name='название ингредиента',
    )
    measurement_unit = models.CharField(
        max_length=200,
        verbose_name='единица измерения',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class RecipeIngredient(models.Model):
    '''
    Модель Ингредиенты в Рецепте:
    recipe - рецепт
    ingredient - ингредиент
    amount - количество ингредиента
    '''

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients',
        verbose_name='рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='ингредиент',
    )
    amount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='количество ингредиента',
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецепте'
