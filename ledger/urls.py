from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView


urlpatterns = [
    path('recipe/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/add_image',
         RecipeUpdateView.as_view(), name='recipe_update'),
]

app_name = "ledger"
