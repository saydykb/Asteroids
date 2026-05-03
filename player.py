import pygame
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED 
from constants import PLAYER_SPEED
from constants import PLAYER_SHOT_SPEED
from constants import PLAYER_SHOT_COOLDOWN_SECONDS
from constants import PLAYER_SIDES_INITIAL
from constants import SHOT_SIDES_INITIAL
from polygonshape import PolygonShape
from shot import Shot

class Player(PolygonShape):
    def __init__( self, x, y ):
        super().__init__( x, y, PLAYER_SIDES_INITIAL, PLAYER_RADIUS)
        self.shot_cooldown_timer = 0
        self.shot_sides = SHOT_SIDES_INITIAL
    
    @property
    def forward(self):
        return pygame.Vector2(0, -1).rotate(self.rotation)
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.vertices, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        self.shot_cooldown_timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
         

    def move(self, dt):
        self.position += self.forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_cooldown_timer > 0:
            pass
        else:
            self.shot_cooldown_timer = PLAYER_SHOT_COOLDOWN_SECONDS
            shot = Shot(self.position.x, self.position.y, self.shot_sides, self.rotation)
            shot.velocity = self.forward
            shot.velocity *= PLAYER_SHOT_SPEED
