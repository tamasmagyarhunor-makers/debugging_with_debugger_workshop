from lib.pokemon_store import *
from lib.pokemon import *

def test_Pokemon_Store_instatiates_with_empty_list():
    pokemon_store = PokemonStore()
    
    actual = pokemon_store.pokemons
    expected = []

    assert actual == expected

def test_can_add_Pokemons_to_Pokemon_Store():
    pokemon_store = PokemonStore()
    pikachu = Pokemon('Pikachu')
    pokemon_store.add(pikachu)

    actual = pokemon_store.pokemons
    expected = [pikachu]

    assert actual == expected
