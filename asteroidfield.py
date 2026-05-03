import pygame 
import random
from asteroid import Asteroid
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from constants import ASTEROID_SPAWN_RATE_SECONDS
from constants import ASTEROID_MAX_RADIUS
from constants import ASTEROID_MIN_SIDES

class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.max_num_sides = 5
        self.game_timer = 0

    def spawn(self, num_sides, position, velocity):
        asteroid = Asteroid(position.x, position.y, num_sides)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        self.game_timer += dt
        if self.game_timer > self.max_num_sides ** 2 * ASTEROID_SPAWN_RATE_SECONDS:
            self.max_num_sides += 1
        if self.spawn_timer > ASTEROID_SPAWN_RATE_SECONDS:
            self.spawn_timer = 0
            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            num_sides = random.randint(ASTEROID_MIN_SIDES, self.max_num_sides)
            self.spawn(num_sides, position, velocity)
