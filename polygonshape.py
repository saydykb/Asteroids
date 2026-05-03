import pygame
import random
from random import randint
# Base class for game objects
class PolygonShape(pygame.sprite.Sprite):
# constructor
    def __init__(self, x, y, number_sides, radius, noise=0, rotation=0):
        if number_sides < 3:
            raise ValueError("Polygons must have at least 3 sides")
        # grabs container init
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
# ATTRIBUTES
# general shape info
        self.number_sides = number_sides
        self.radius = radius
# generate local shape
        self.shape = self._generate_polygon(radius, noise)
        self.shape_normals = self._calculate_normals()
# get shape position
        self.position = pygame.Vector2(x, y)
# get shape rotation
        self.rotation = rotation
# get shape velocity vector
        self.velocity = pygame.Vector2(0, 0)
# cached attributes
        self._last_position_for_vertices = self.position.copy()
        self._last_rotation_for_vertices = self.rotation
        self._last_rotation_for_normals = self.rotation
# cached properties
        self._cached_vertices = [self.position + point.rotate(self.rotation) for point in self.shape]
        self._cached_normals = [normal.rotate(self.rotation) for normal in self.shape_normals]
# PROPERTIES
    @property 
    def vertices(self):
        if self.rotation != self._last_rotation_for_vertices or self.position != self._last_position_for_vertices:
            self._last_rotation_for_vertices = self.rotation
            self._last_position_for_vertices = self.position.copy()
            self._cached_vertices = [self.position + point.rotate(self.rotation) for point in self.shape]
            return self._cached_vertices
        else:
            return self._cached_vertices
    
    @property
    def normals(self):
        if self.rotation != self._last_rotation_for_normals:
            self._cached_normals = [normal.rotate(self.rotation) for normal in self.shape_normals]
            self._last_rotation_for_normals = self.rotation
            return self._cached_normals
        else:
            return self._cached_normals
# helper functions for properteis
    def _generate_polygon(self, radius, noise):
        avg_angle = 360 / self.number_sides
        points = [
                pygame.Vector2(0,-1).rotate( (avg_angle * i) ) * 
                radius * ( 1 + random.uniform(-noise,noise) )
                for i in range(self.number_sides)
                ]
        return points

    def _calculate_edges(self):
        edges = []
        for i in range(len(self.shape)):
            edges.append( self.shape[i] - self.shape[i-1] )
        return edges

    def _calculate_normals(self, edges=None):
        if edges is None:
            edges = self._calculate_edges()
        return [edge.rotate(90).normalize() for edge in edges]
# shape logic 
    def collides_with(self, other):

        normals = self.normals + other.normals
        self_vertices = self.vertices
        other_vertices = other.vertices

        for normal in normals:
            
            self_min = self_max = self_vertices[0].dot(normal)
            for vertex in self_vertices[1:]:
                projection = vertex.dot(normal)
                self_min = min(self_min, projection)
                self_max = max(self_max, projection)

            other_min = other_max = other_vertices[0].dot(normal)
            for vertex in other_vertices[1:]:
                projection = vertex.dot(normal)
                other_min= min(other_min, projection)
                other_max = max(other_max, projection)

            if self_max < other_min or self_min > other_max:
                return False
        return True
# methods to be overridden                 
    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
