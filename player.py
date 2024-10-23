import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, \
    PLAYER_SHOOT_COOLDOWN


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cd = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.shot_cd > 0:
            self.shot_cd -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_cd <= 0:
            shot = Shot(self.position.x, self.position.y)
            fly = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = fly * PLAYER_SHOOT_SPEED
            self.shot_cd += PLAYER_SHOOT_COOLDOWN


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, center=self.position, radius=self.radius, width=2, color="blue")

    def update(self, dt):
        self.position = self.position + self.velocity * dt
