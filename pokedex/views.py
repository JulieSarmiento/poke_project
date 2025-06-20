from django.http import JsonResponse, Http404
from .models import Pokemon

## display the list of pokemon
def pokemon_list_api(request):
    data = list(Pokemon.objects.all().values("api_id", "name", "types", "image_url"))
    return JsonResponse(data, safe=False)


## display the detail of a pokemon
def pokemon_detail_api(request, api_id):
    try:
        pokemon = Pokemon.objects.get(api_id=api_id)
    except Pokemon.DoesNotExist:
        raise Http404("Pokemon not found")

    data = {
        "api_id": pokemon.api_id,
        "name": pokemon.name,
        "types": pokemon.types,
        "image_url": pokemon.image_url,
    }
    return JsonResponse(data)
    