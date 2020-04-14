import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("corona go")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 500

# Draw the player


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game loop
running = True
while running:
    # Background
    screen.fill((255, 0, 0))
    playerX += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Calling player
    player(playerX, playerY)
    pygame.display.update()
