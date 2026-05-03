import pygame
import random
from random import randint
# Base class for game objects
class PolygonShape(pygame.sprite.Sprite):

    def __init__(self, x, y, number_sides, radius, noise=0, rotation=0):
        if number_sides < 3:
            raise ValueError("Polygons must have at least 3 sides")
        # grabs container init
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.number_sides = number_sides
        self.radius = radius
        self.rotation = rotation
        self.shape = self._generate_polygon(radius, noise)

    @property 
    def verticies(self):
        return [self.position + point.rotate(self.rotation) for point in self.shape]
    
    def _generate_polygon(self, radius, noise):
        avg_angle = 360 / self.number_sides
        points = [
                pygame.Vector2(0,-1).rotate( (avg_angle * i) ) * 
                radius * ( 1 + random.uniform(-noise,noise) )
                for i in range(self.number_sides)
                ]
        return points

    def collides_with(self, other):
        # do later
        pass

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
