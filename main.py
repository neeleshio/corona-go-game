import pygame
import random

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
playerX_change = 0

# Enemy (Random value to appear in random places)
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)


# Draw the player
def player(x, y):
    screen.blit(playerImg, (x, y))
    
# Draw the enemy
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game loop
running = True
while running:
    # Background
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #Movement
    playerX += playerX_change

    #Adding boundaries
    if playerX <= 0:
        playerX = 0
    if playerX >=736:
        playerX = 736

    # Calling player
    player(playerX, playerY)
    # Calling enemy
    enemy(enemyX, enemyY)

    pygame.display.update()

