from django.contrib import admin
from .models import Pokemon, Favorite, Note, Tag

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', "api_id", "types")


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "pokemon", "created_at")
    list_filter = ("user",)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("user", "pokemon", "created_at")
    search_fields = ("texts",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    filter_horizontal = ("pokemons",)