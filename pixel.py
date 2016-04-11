import pygame


class Pixel:
    location = (0, 0)
    color = (255, 0, 0)
    size = 2
    type = 0

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def draw(self):
        pygame.draw.circle(
                self.screen,
                self.color,
                self.location,
                self.size,
                self.type)
