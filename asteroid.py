import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 
                           "white", 
                           self.position, 
                           self.radius, 
                           LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20, 50)
            split_velocity_1 = self.velocity.rotate(split_angle)
            split_velocity_2 = self.velocity.rotate(-split_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            split_asteroid_1 = Asteroid(self.position.x, 
                                        self.position.y, 
                                        new_asteroid_radius)
            split_asteroid_2 = Asteroid(self.position.x,
                                        self.position.y,
                                        new_asteroid_radius)
            split_asteroid_1.velocity = split_velocity_1 * 1.2
            split_asteroid_2.velocity = split_velocity_2 * 1.2

