import pygame

from pygame.locals import *
from dot import Dot
from matrix import Matrix
from board import Board


# TODO: get image from API
mars_map = Matrix()
mars_map.open()
mars_map.edit()
mars_map.save()
mars_map.get_matrix()

map_pixel = mars_map.size()

pygame.init()

# GLOBAL VARIABLES
MAX_ANTS = 500
speed = 10
tp = 0
ant_lst = []

# pygame CONFIG
screen_size = mars_map.size()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
done = False
run = False
can_change = True
map_path = mars_map.rendered_map
# bg = pygame.image.load(map_path).convert()
board = Board(matrix=mars_map.matrix, screen=screen)
board.backup()

clock = pygame.time.Clock()
start_point = None
end_point = None

# board.draw()

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                run = not run
                can_change = False

    # screen.blit(bg, [0, 0])

    key = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    pos_mouse = pygame.mouse.get_pos()

    if mouse[0] and can_change:
        if start_point is None:
            start_point = Dot(
                    location=pos_mouse,
                    screen=screen,
                    type=0)
        else:
            start_point.location = pos_mouse
    if mouse[2] and can_change:
        if end_point is None:
            end_point = Dot(
                    location=pos_mouse,
                    screen=screen,
                    type=2)
        else:
            end_point.location = pos_mouse

    if start_point is not None:
        start_point.draw()
    if end_point is not None:
        end_point.draw()

    if not can_change:
        board.generate_ants(MAX_ANTS)

    board.draw()

    pygame.display.flip()

pygame.quit()
