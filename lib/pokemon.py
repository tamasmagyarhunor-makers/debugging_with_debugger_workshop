from lib.bag import *

class Pokemon():
    def __init__(self, name, bag = Bag()) -> None:
        self.name = name
        self.bag = bag