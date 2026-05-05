import pygame
from gamestate import GameState
from menustate import MenuState
from playstate import PlayState

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.state = None
        self._running = False

    def change_state(self, new_state):
        if new_state == "play":
            self.state = PlayState(self)
        if new_state == "menu":
            self.state = MenuState(self)

    def run(self):
        if self.state is None:
            self.state = MenuState(self)
        self._running = True
        
        while self._running:
            self.state.game_loop()
