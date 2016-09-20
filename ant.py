import random

from pixel import Pixel


class Ant(Pixel):
    pos_list = []

    def __init__(self, **kwargs):
        self.smart = random.randint(0, 100)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def move(self):
        # TODO: self.location by the moment all ants
        # are stupid without a purpose
        x = self.location[0] + random.randint(-5, 5)
        y = self.location[1] + random.randint(-5, 5)
        self.location = (x, y)
        pass
