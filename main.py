# This allows us to use code from the open source pygame library throughout this file
import pygame as pg
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0.0

    shots = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        screen.fill("black")
        
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                return                
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pg.display.flip()
        
        
        dt = clock.tick(60)/1000.0

if __name__ == "__main__":
    main()
