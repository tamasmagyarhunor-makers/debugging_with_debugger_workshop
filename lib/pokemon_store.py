class PokemonStore():
    def __init__(self) -> None:
        self.pokemons = []

    def add(self, pokemon):
        self.pokemons.append(pokemon)