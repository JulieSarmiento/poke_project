from django.urls import path
from .views import pokemon_list_api

## urls for pokemon detail
urlpatterns = [
    path("pokemon/", pokemon_list_api, name="pokemon_list"),
]