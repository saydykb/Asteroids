import pygame
import sys
from logger import log_event
from gamestate import GameState
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT

class PlayState(GameState):

    def __init__(self, screen, clock):
        super().__init__(screen, clock)
    # add groups
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
    # add objects to groups
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.updatable,)
        Player.containers = (self.updatable, self.drawable)
        Shot.containers = (self.shots, self.updatable, self.drawable)
    # instantiate objects
        self.asteroid_field = AsteroidField()
        self.player = Player( SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2 )

    def state_loop(self):
        for asteroid in self.asteroids:
               if self.player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in self.asteroids:
            for shot in self.shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

