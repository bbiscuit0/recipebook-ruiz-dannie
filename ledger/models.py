from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=255, default='author')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)

    ingredient = models.ForeignKey(Ingredient,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='recipe'
                                   )

    recipe = models.ForeignKey(Recipe,
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name='ingredients'
                               )

    def __str__(self):
        return f'{self.ingredient} : {self.quantity} in {self.recipe}'


class RecipeImage(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True)

    recipe = models.ForeignKey(Recipe,
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name='images'
                               )

    def __str__(self):
        return f'{self.description}'
