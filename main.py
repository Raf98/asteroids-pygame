# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from start_screen import StartScreen
from game_over_screen import GameOverScreen

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2

    start = StartScreen(screen, center_x, center_y)
    start.draw_start_screen()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    
    player = Player(center_x, center_y)
    asteroid_field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        updatable.update(dt)

        screen.fill("black")
        for draw_obj in drawable:
            draw_obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                running = False
                break
            
            for bullet in shots:
                if asteroid.collides_with(bullet):
                    asteroid.split()
                    bullet.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


    game_over = GameOverScreen(screen, center_x, center_y)
    game_over.draw_game_over_screen()


if __name__ == "__main__":
    main()
