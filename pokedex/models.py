from django.db import models
from django.contrib.auth.models import User

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    api_id = models.PositiveIntegerField(unique=True)
    image_url = models.URLField(blank=True)
    types = models.CharField(max_length=100, blank=True)

    ## string representation of the model, returns the name of the pokemon
    def __str__(self):
        return self.name.capitalize()

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'pokemon')

    def __str__(self):
        return f'{self.user.username} ❤️ {self.pokemon.name}'


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F'Note by {self.user.username} on {self.pokemon.name}'


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    pokemons = models.ManyToManyField(Pokemon, related_name='tags')

    def __str__(self):
        return f'{self.name} ({self.user.username})'


    