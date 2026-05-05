import pygame
import sys
from logger import log_state
from constants import DEFAULT_SCREEN_COLOR
from constants import FPS

class GameState:
    
    def __init__(self, game):
        self.game = game
        self.screen_color = DEFAULT_SCREEN_COLOR
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.dt = 0
        self.time = 0
        self.fps = FPS
        self.next_state = False

    def game_loop(self):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        self.updatable.update(self.dt)
        self.state_loop()
        self.game.screen.fill(self.screen_color)
        for drawing in self.drawable:
            drawing.draw(self.game.screen)
        pygame.display.flip()
        self.dt = self.game.clock.tick(self.fps) / 1000
        return None

    def state_loop(self):
        # override this if have custom behavior for the game loop
        pass
