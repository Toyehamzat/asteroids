import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create font for text rendering
    font = pygame.font.Font(None, 74)
    game_over = False

    # Create groups for game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set up containers for automatic group assignment
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Create player and add to groups
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    updatable.add(player)
    drawable.add(player)

    # Create asteroid field
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        # Handle events (check if user closed window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable objects (only if game is not over)
        if not game_over:
            for obj in updatable:
                obj.update(dt)

        # Check for collisions between player and asteroids
        if not game_over:
            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    game_over = True
                    break

        # Check for collisions between shots and asteroids
        if not game_over:
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collides_with(shot):
                        asteroid.split()
                        shot.kill()
                        break

        # Fill screen with black
        screen.fill("black")

        # Draw all drawable objects
        for obj in drawable: 
            obj.draw(screen)
        
        # Draw game over text if game is over
        if game_over:
            game_over_text = font.render("GAME OVER", True, "white")
            play_again_text = font.render("Press R to Restart", True, "white")
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(game_over_text, text_rect)
            play_again_rect = play_again_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            screen.blit(play_again_text, play_again_rect)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game_over = False
                # Reset game state
                for asteroid in asteroids:
                    asteroid.kill()
                for shot in shots:
                    shot.kill()
                player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                player.velocity = pygame.Vector2(0, 0)
                player.rotation = 0
                player.timer = 0

        # Refresh the screen
        pygame.display.flip()

        # Limit to 60 FPS
        dt = clock.tick(60) / 1000  # dt is in milliseconds


if __name__ == "__main__":
    main()
