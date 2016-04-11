import pygame

from ant import Ant


class Board:
    ant_list = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def backup(self):
        # print self.matrix
        self.backup_matrix = self.matrix

    def draw(self):
        for x, raw in enumerate(self.matrix):
            for y, pixel in enumerate(raw):
                # print raw
                # pass
                # print "color: {} x: {} y: {}".format(pixel, x, y)
                # import pdb; pdb.set_trace()
                self.screen.blit((0, 255, 0), (x, y))

    def generate_ants(self, number=500):
        for i in range(number):
            self.ant_list.append(Ant(location=self.location))
