import pygame
import sys
from logger import log_state
from constants import SCREEN_COLOR
from constants import FPS

class GameState:
    
    def __init__(self, screen, clock):
        self.screen_color = SCREEN_COLOR
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.dt = 0
        self.time = 0
        self.fps = FPS
        self.clock = clock
        self.screen = screen
        
    def game_loop(self):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        self.updatable.update(self.dt)
        self.state_loop()
        self.screen.fill(self.screen_color)
        for drawing in self.drawable:
            drawing.draw(self.screen)
        pygame.display.flip()
        self.dt = self.clock.tick(self.fps) / 1000

    def state_loop(self):
        # override this
        pass
