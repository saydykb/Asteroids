import pygame
import sys
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set fps
    clock = pygame.time.Clock()
    dt = 0

# groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
# instantiate asteroid field object
    asteroid_field = AsteroidField()
# instantiate player object
    player = Player( SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
# game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
