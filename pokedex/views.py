from django.http import JsonResponse
from .services import get_pokemon

def pokemon_detail(request, api_id: int):
    pokemon = get_pokemon(api_id)
    if not pokemon:
        return JsonResponse({"error": f"Pokémon {api_id} not found"}, status=404)

    return JsonResponse({
        "name": pokemon.name,
        "api_id": pokemon.api_id,
        "types": pokemon.types,
        "image_url": pokemon.image_url
    })