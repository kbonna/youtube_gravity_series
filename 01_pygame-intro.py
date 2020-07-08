import pygame
import sys

colors = {
    'blue': (135, 206, 235)
}

pygame.init()

win_size = (500, 500)
win = pygame.display.set_mode(win_size)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.circle(win, colors['blue'], (250, 250), 15)
    pygame.display.flip()