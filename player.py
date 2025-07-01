import circleshape
import pygame as pg
from constants import *
import shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pg.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    
    def move(self, dt):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.rotate(-dt)

        if keys[pg.K_d]:
            self.rotate(dt)

        if keys[pg.K_w]:
            self.move(dt)
        
        if keys[pg.K_s]:
            self.move(-dt)
        
        if keys[pg.K_SPACE]:
            return self.shoot()

    def shoot(self):
        shot_position = self.position + pg.Vector2(0, 1).rotate(self.rotation) * self.radius
        new_shot = shot.Shot(shot_position.x, shot_position.y, SHOT_RADIUS)
        new_shot.velocity = pg.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        return new_shot