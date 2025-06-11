from django.urls import path
from . import views

urlpatterns = [
    path("pokemon/<int:api_id>/", views.pokemon_detail),
]