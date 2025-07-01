import circleshape
import pygame as pg
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pg.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        newAngle = random.uniform(20,50)
        newVelocity1 = self.velocity.rotate(newAngle)
        newVelocity2 = self.velocity.rotate(-newAngle)
        newRadius= self.radius - ASTEROID_MIN_RADIUS
        newAsteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
        newAsteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
        newAsteroid1.velocity = newVelocity1*1.2
        newAsteroid2.velocity = newVelocity2*1.2
        return newAsteroid1, newAsteroid2
        