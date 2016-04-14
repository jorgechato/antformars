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
                pass

    def generate_ants(self, location, end_point, number_of_ants=500):
        for i in range(number_of_ants):
            self.ant_list.append(Ant(
                location=location,
                end_pint=end_point,
                screen=self.screen))

    def draw_ants(self):
        for ant in self.ant_list:
            ant.draw()

    def move_ants(self):
        for ant in self.ant_list:
            ant.move()
