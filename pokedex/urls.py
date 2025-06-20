from django.urls import path
from .views import pokemon_list_api, pokemon_detail_api

## urls for pokemon detail
urlpatterns = [
    path("api/pokemon/", pokemon_list_api, name="pokemon_list"),
    path("api/pokemon/<int:api_id>/", pokemon_detail_api, name="pokemon_detail"),
]