import os
import numpy as np

from PIL import Image
from PIL import ImageFilter
# from PIL import ImageEnhance


class Matrix:
    name = "map.jpg"
    max_size = 1000

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def open(self):
        raw_map = os.path.join("res/raw", self.name)
        self.image = Image.open(raw_map)

    def edit(self):
        self.image = self.image.filter(ImageFilter.FIND_EDGES)
        # self.image = self.image.convert('L')

        self.matrix = np.asarray(self.image).copy()

        self.matrix[self.matrix < 128] = 0
        self.matrix[self.matrix >= 128] = 255

        self.image = Image.fromarray(self.matrix)
        self.image.thumbnail((self.max_size, self.max_size))
        self.matrix = np.array(self.image).copy().tolist()

    def save(self):
        self.rendered_map = os.path.join("res/rendered", self.name)
        self.image.save(self.rendered_map)

    def size(self):
        return self.image.size
