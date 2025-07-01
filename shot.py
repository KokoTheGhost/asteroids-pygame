import circleshape
import pygame as pg
from constants import *

"""Create a new Shot class to represent a bullet. It should also inherit from CircleShape so that it can use our collision detection code. It should look very similar to our Asteroid class in that it will be drawn and have its position updated. Use a new SHOT_RADIUS constant and set it to 5.
Set up a new group in your initialization code and make it contain all of your shots."""

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pg.Vector2(0, 0)

    def draw(self, screen):
        pg.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), SHOT_RADIUS, width=2)

    def update(self, dt):
        self.position += self.velocity * dt