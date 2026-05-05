import pygame
from gamestate import GameState
from text import Text
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import H_CENTER
from constants import V_CENTER

class MenuState(GameState):

    def __init__(self, game):
        super().__init__(game)
    # add groups
        self.menu_items = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
    # add objects to groups
        Text.containers = (self.menu_items, self.drawable, self.updatable)
        Asteroid = (self.asteroids, self.drawable, self.updatable)
    # instantiate objects
        spacer = 50
        self.asteroid_field = AsteroidField
        self.title = Text(H_CENTER, V_CENTER, "ASTEROIDS", 96, True)
        self.menu = Text(H_CENTER, V_CENTER, "press enter to start", 24)
    # move objects to position
        self.title.position.y -= self.title.height / 2 + spacer
        self.menu.position.y += self.menu.height / 2 + spacer
    # animation timer
        self.animation_timer = 0

    def state_loop(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.game.change_state("play")
        self.animation_timer += self.dt
        if self.animation_timer >= 1:
            if self.menu.visible:
                self.menu.visible = False
                self.animation_timer = 0
            else:
                self.menu.visible = True
                self.animation_timer = 0   
