import pygame
from polygonshape import PolygonShape
from constants import SHOT_RADIUS
from constants import LINE_WIDTH

class Shot(PolygonShape):
    def __init__(self, x, y, num_sides, rotation):
        super().__init__(x, y, num_sides, SHOT_RADIUS, 0, rotation)

    def draw(self, screen):
        pygame.draw.polygon(screen,
                            "white",
                            self.vertices,
                            LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
