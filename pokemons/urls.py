from django.urls import path
from .views import PokemonListView,PokemonDetailView,PokemonCreateView,PokemonUpdateView,PokemonDeleteView 

urlpatterns=[
    path('pokemon/',PokemonListView.as_view(),name='pokemon_list'),
    path('pokemon/<int:pk>/',PokemonDetailView.as_view(),name='pokemon_detail'),
    path('pokemon/create/',PokemonCreateView.as_view(),name="pokemon_create"),
    path ('pokemon/<int:pk>/update/',PokemonUpdateView.as_view(),name='pokemon_update'),
    path('pokemon/<int:pk>/delete/',PokemonDeleteView.as_view(),name='pokemon_delete')
]