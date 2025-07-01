# This allows us to use code from the open source pygame library throughout this file
import pygame as pg
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0.0

    asteroids = pg.sprite.Group()
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()

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
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pg.display.flip()
        
        
        dt = clock.tick(60)/1000.0

if __name__ == "__main__":
    main()
