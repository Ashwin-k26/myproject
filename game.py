#create a simple 3D game where the player has to move the
#character to the right side of the screen to win. The player can move left
#, right, up, and down using the arrow keys. The game should end
#when the player reaches the right side of the screen to win and there should
# be a some obstacles in the middle of the screen that the player has to avoid.
import pygame
import random
# Initialize Pygame
pygame.init()
# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple 3D Game")
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
# Define player properties
player_size = 50
player_x = 50
player_y = HEIGHT // 2 - player_size // 2
player_speed = 5
# Define obstacle properties
obstacle_size = 50
obstacle_x = random.randint(WIDTH // 2, WIDTH - obstacle_size)
obstacle_y = random.randint(0, HEIGHT - obstacle_size)
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    # Check for collision with obstacle
    if (player_x < obstacle_x + obstacle_size and
        player_x + player_size > obstacle_x and
        player_y < obstacle_y + obstacle_size and
        player_y + player_size > obstacle_y):
        print("Game Over! You hit an obstacle.")
        running = False
    # Check for win condition
    if player_x + player_size >= WIDTH:
        print("Congratulations! You win!")
        running = False
    # Fill the background
    screen.fill(WHITE)
    # Draw the player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_size, player_size))
    # Draw the obstacle
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))
    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()