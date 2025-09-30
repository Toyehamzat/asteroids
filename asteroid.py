import pygame
import random
import math
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Generate a random shape for this asteroid
        self.shape_points = self._generate_shape()

    def _generate_shape(self):
        """Generate a random irregular polygon shape for the asteroid"""
        # Number of points for the polygon (between 6 and 12)
        num_points = random.randint(6, 12)
        points = []
        
        for i in range(num_points):
            # Calculate angle for this point
            angle = (2 * math.pi * i) / num_points
            
            # Add some randomness to the radius (between 0.7 and 1.3 times the base radius)
            radius_variation = random.uniform(0.7, 1.3)
            point_radius = self.radius * radius_variation
            
            # Calculate the point position relative to center
            x = point_radius * math.cos(angle)
            y = point_radius * math.sin(angle)
            points.append((x, y))
        
        return points

    def draw(self, screen):
        # Convert relative points to absolute screen coordinates
        absolute_points = []
        for x, y in self.shape_points:
            abs_x = self.position.x + x
            abs_y = self.position.y + y
            absolute_points.append((abs_x, abs_y))
        
        # Draw the polygon outline
        if len(absolute_points) >= 3:
            pygame.draw.polygon(screen, "white", absolute_points, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Calculate new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create 2 new vectors rotated by random_angle and -random_angle
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        
        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set their velocities to split in opposite directions
        asteroid1.velocity = velocity1 * 1.2  # Make them move a bit faster
        asteroid2.velocity = velocity2 * 1.2

