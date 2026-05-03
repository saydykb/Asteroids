import pygame
import random
from logger import log_event
from polygonshape import PolygonShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_SIDES
from constants import ASTEROID_NOISE
from constants import ASTEROID_MIN_RADIUS

class Asteroid(PolygonShape):

    def __init__(self, x, y, number_sides):
        super().__init__(x, y, number_sides, ASTEROID_MIN_RADIUS * number_sides, ASTEROID_NOISE, random.uniform(0, 360))

    def draw(self, screen):
        pygame.draw.polygon(screen, 
                           "white", 
                           self.vertices, 
                           LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.number_sides <= ASTEROID_MIN_SIDES:
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20, 50)
            split_velocity_1 = self.velocity.rotate(split_angle)
            split_velocity_2 = self.velocity.rotate(-split_angle)
            new_asteroid_sides = self.number_sides - 1
            split_asteroid_1 = Asteroid(self.position.x, 
                                        self.position.y, 
                                        new_asteroid_sides)
            split_asteroid_2 = Asteroid(self.position.x,
                                        self.position.y,
                                        new_asteroid_sides)
            split_asteroid_1.velocity = split_velocity_1 * 1.2
            split_asteroid_2.velocity = split_velocity_2 * 1.2

