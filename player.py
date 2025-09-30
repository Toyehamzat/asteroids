import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # Decrease the timer by dt every frame
        if self.timer > 0:
            self.timer -= dt

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-dt)  # Negative dt to rotate left
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(dt)   # Positive dt to rotate right
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE] or keys[pygame.K_KP_ENTER]:
             self.shoot()

    def shoot(self):
        # Prevent shooting if timer is greater than 0
        if self.timer > 0:
            return
            
        # Create a new shot at the position of the player
        shot = Shot(self.position.x, self.position.y)
        
        # Set the shot's velocity:
        # Start with a pygame.Vector2 of (0, 1)
        velocity = pygame.Vector2(0, 1)
        # Rotate it in the direction the player is facing
        velocity = velocity.rotate(self.rotation)
        # Scale it up (multiply by PLAYER_SHOOT_SPEED) to make it move faster
        shot.velocity = velocity * PLAYER_SHOOT_SPEED
        
        # Set the cooldown timer
        self.timer = PLAYER_SHOOT_COOLDOWN
    
