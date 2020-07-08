import math
import pygame
import sys

colors = {
    'blue': (135, 206, 235),
    'black': (0, 0, 0),
    'yellow': (249, 215, 28)
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

class Simulation:
    dt = 0.01
    g = 0.001

    def __init__(self, planet_list, win_size):
        pygame.init()
        self.win = pygame.display.set_mode(win_size)
        self.planet_list = planet_list

    def calculate_acceleration(self):
        for planet in self.planet_list:
            planet.calculate_acceleration(self.planet_list, self.g)

    def update(self):
        for planet in self.planet_list:
            planet.update(self.dt)

    def draw(self):
        for planet in self.planet_list:
            planet.draw(self.win)

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.win.fill(colors['black'])
            self.calculate_acceleration()
            self.update()
            self.draw()
            pygame.display.flip()

star1 = Planet(
    pos=Vector(200, 500),
    vel=Vector(0, 1),
    mass=1_000_000,
    radius=25,
    color=colors['yellow']
)
star2 = Planet(
    pos=Vector(600, 500),
    vel=Vector(0, -1),
    mass=1_500_000,
    radius=30,
    color=colors['yellow']
)
p1 = Planet(
    pos=Vector(250, 500),
    vel=Vector(0, 5),
    radius=5,
    mass=1
)
p2 = Planet(
    pos=Vector(120, 500),
    vel=Vector(0, -3),
    radius=10,
    mass=4
)
p3 = Planet(
    pos=Vector(600, 350),
    vel=Vector(2.5, 0),
    radius=15,
    mass=8
)

sim = Simulation([star1, star2, p1, p2, p3], (800, 800))
sim.run()