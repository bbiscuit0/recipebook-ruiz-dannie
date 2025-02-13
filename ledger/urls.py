from django.urls import path
from .views import index, recipe_list, recipe1, recipe2

urlpatterns = [
    path('', index, name='index'),
    path('recipe/list', recipe_list, name='recipe_list'),
    path('recipe/1', recipe1, name='recipe1'),
    path('recipe/2', recipe2, name='recipe2'),
]

app_name = "ledger"