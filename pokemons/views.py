from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Pokemon
# Create your views here.

class PokemonListView(ListView):
    template_name='pokemon/pokemon_list.html'
    model = Pokemon

class PokemonDetailView(DetailView):
    template_name="pokemon/pokemon_detail.html"
    model= Pokemon

class PokemonCreateView(CreateView):
    template_name="pokemon/pokemon_create.html"
    model= Pokemon
    fields=['pokemon', 'pokemon_type', 'owner','description','img_url']

class PokemonUpdateView(UpdateView):
    template_name="pokemon/pokemon_update.html"
    model= Pokemon
    fields=['pokemon', 'pokemon_type', 'owner','description','img_url']

class PokemonDeleteView(DeleteView):
    template_name='pokemon/pokemon_delete.html'
    model= Pokemon
    success_url=reverse_lazy('pokemon_list')