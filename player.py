import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.player_shoot_cooldown = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if self.player_shoot_cooldown > 0:
            self.player_shoot_cooldown -= dt
            if self.player_shoot_cooldown < 0:
                self.player_shoot_cooldown = 0

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.rotate(-dt)
        if keys[pygame.K_d]  or keys[pygame.K_RIGHT]:
                self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
             self.move(dt)
        if keys[pygame.K_s]  or keys[pygame.K_DOWN]:
             self.move(-dt)
        if keys[pygame.K_SPACE]:
             self.shoot()

    def move(self, dt):
         unit_vector = pygame.Vector2(0, 1)
         rotated_vector = unit_vector.rotate(self.rotation)
         rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
         self.position += rotated_with_speed_vector

    def shoot(self):
        if self.player_shoot_cooldown > 0:
            return
        
        self.player_shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        new_shot = Shot(self.position.x, self.position.y)
        shot_vector = pygame.Vector2(0, 1)
        rotated_shot = shot_vector.rotate(self.rotation)
        new_shot_speed = rotated_shot * PLAYER_SHOOT_SPEED
        new_shot.velocity = new_shot_speed
