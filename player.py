import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
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
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.rotate(-dt)
        if keys[pygame.K_d]  or keys[pygame.K_RIGHT]:
                self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
             self.move(dt)
        if keys[pygame.K_s]  or keys[pygame.K_DOWN]:
             self.move(-dt)

    def move(self, dt):
         unit_vector = pygame.Vector2(0, 1)
         rotated_vector = unit_vector.rotate(self.rotation)
         rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
         self.position += rotated_with_speed_vector

    def shoot(self):
         new_shot = Shot(self.x, self.y, SHOT_RADIUS)
         PLAYER_SHOOT_SPEED

            # Start with a base direction vector.
            # Rotate that vector by the player's current rotation.
            # Scale that rotated vector by the desired speed.
            # Assign this final vector to the velocity attribute of your new_shot object.