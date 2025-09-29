import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create groups for game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Create player and add to groups
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    updatable.add(player)
    drawable.add(player)

    
    # Game loop
    while True:
        # Handle events (check if user closed window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)
        
        # Fill screen with black
        screen.fill("black")

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        
        # Refresh the screen
        pygame.display.flip()
        
        # Limit to 60 FPS
        dt = clock.tick(60)/1000  # dt is in milliseconds

    


if __name__ == "__main__":
    main()
