from bag import *

class Pokemon():
    def __init__(self, name, bag = Bag()) -> None:
        self.name = name
        self.bag = bag

    def add_food(self, food):
        self.bag.add_to_space(food)


pokemon = Pokemon('Venusaur')
pokemon.add_food('Rocks')

food_space = pokemon.bag.space