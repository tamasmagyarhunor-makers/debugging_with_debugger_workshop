from lib.pokemon import *

def test_Pokemon_takes_argument_for_name():
    pokemon = Pokemon('Pikachu')

    actual = pokemon.name
    expected = 'Pikachu'

    assert actual == expected

def test_Pokemon_instantiates_with_a_Bag():
    pokemon = Pokemon('Bulbasaur')

    actual = type(pokemon.bag)
    expected = Bag

    assert actual == expected