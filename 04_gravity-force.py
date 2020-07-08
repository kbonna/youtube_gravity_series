import math
import pygame
import sys

colors = {
    'blue': (135, 206, 235),
    'black': (0, 0, 0)
}

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    @property
    def grid_coords(self):
        return (round(self.x), round(self.y))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


class Planet:

    def __init__(self, pos, vel, mass, color=colors['blue'], radius=15):
        self.pos = pos
        self.vel = vel
        self.acc = Vector(0, 0)
        self.mass = mass
        self.color = color
        self.radius = radius

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos.grid_coords, self.radius)

    def calculate_acceleration(self, planet_list, g):
        acc_components = []
        for planet in planet_list:
            if planet != self:
                r_vec = planet.pos - self.pos
                r = abs(r_vec)
                acc = g * planet.mass / r ** 3 * r_vec
                acc_components.append(acc)
        self.acc = sum(acc_components, start=Vector(0, 0))

    def update(self, dt):
        self.pos = self.pos + self.vel * dt + 0.5 * self.acc * dt ** 2
        self.vel = self.vel + self.acc * dt

p1 = Planet(
    pos=Vector(150, 250),
    vel=Vector(0, 5),
    mass=1
)
p2 = Planet(
    pos=Vector(350, 250),
    vel=Vector(0, -5),
    mass=1
)
planet_list = [p1, p2]

pygame.init()

win_size = (500, 500)
win = pygame.display.set_mode(win_size)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    win.fill(colors['black'])

    for planet in planet_list:
        planet.calculate_acceleration(planet_list, 0)
    for planet in planet_list:
        planet.update(0.01)
    for planet in planet_list:
        planet.draw(win)

    pygame.display.flip()