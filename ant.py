import random

from pixel import Pixel


class Ant(Pixel):
    pos_list = []

    def __init__(self, **kwargs):
        self.smart = random.randint(0, 100)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def move(self):
        # TODO: self.location
        pass
