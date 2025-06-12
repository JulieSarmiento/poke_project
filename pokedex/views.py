from django.http import JsonResponse
from django.shortcuts import render
from .models import Pokemon
from .services import get_pokemon

## display the list of pokemon
def pokemon_list_api(request):
    data = list(Pokemon.objects.all().values("api_id", "name", "types", "image_url"))
    return JsonResponse(data, safe=False)
