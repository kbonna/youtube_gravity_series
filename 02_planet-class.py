import pygame
import sys

colors = {
    'blue': (135, 206, 235),
    'black': (0, 0, 0)
}

class Planet:

    def __init__(self, pos, vel, mass, color=colors['blue'], radius=15):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.color = color
        self.radius = radius

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos_grid, self.radius)

    @property
    def pos_grid(self):
        return (round(self.pos[0]), round(self.pos[1]))

    def update(self, dt):
        # new_pos = self.pos + self.vel * dt
        new_pos = (self.pos[0] + self.vel[0] * dt, 
                   self.pos[1] + self.vel[1] * dt)
        self.pos = new_pos

p1 = Planet(
    pos=(250, 250),
    vel=(-15, -15),
    mass=1
)

pygame.init()

win_size = (500, 500)
win = pygame.display.set_mode(win_size)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    win.fill(colors['black'])
    p1.update(0.001)
    p1.draw(win)
    pygame.display.flip()