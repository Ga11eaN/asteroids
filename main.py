import pygame

import sys

from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids_group, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable, )
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids_group:
            if player.collision(obj):
                print("Game over!")
                sys.exit(0)
            for bul in shots:
                if bul.collision(obj):
                    obj.split()
                    bul.kill()

        screen.fill(color="black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()