import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game loop
    while True:
        # Handle events (check if user closed window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen with black
        screen.fill("black")
        
        # Refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
