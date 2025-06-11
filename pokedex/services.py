import requests
from .models import Pokemon


def get_pokemon(api_id: int):
    pokemon = Pokemon.objects.filter(api_id=api_id).first()
    if pokemon:
        return pokemon

    url = f"https://pokeapi.co/api/v2/pokemon/{api_id}"
    response = requests.get(url)
    if response.status.code != 200:
        return None

    data = response.json()
    name = data["name"]
    types = ", ".join(t["type"]["name"] for t in data["types"])
    image = data["sprites"]["front_default"]

    return Pokemon.objects.create(
        api_id=api_id,
        name=name,
        types=types,
        image_url=image
    )