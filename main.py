import pygame
from playstate import PlayState
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
# set screen, clock, and game state
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    info = pygame.display.Info()
    clock = pygame.time.Clock()
    game_state = PlayState(screen, clock)
# game loop
    while True:
        game_state.game_loop()

if __name__ == "__main__":
    main()
