class Bag():
    def __init__(self) -> None:
        self.space = []

    def add_to_space(self, food):
        self.space.append(food)