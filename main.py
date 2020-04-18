import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen & backgrond
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png')

# Sounds
# mixer.music.load('bmusic.wav')
# mixer.music.play(-1)

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0 
bulletY = 500
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

 # Score variable
score_value = 0
font = pygame.font.Font('Minecrafter_3.ttf', 27)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('Minecrafter_3.ttf', 60)

# Draw the player
def player(x, y):
    screen.blit(playerImg, (x, y))

# Draw an enemy
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Bullet fire
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

# Collision
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else: return False

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("Stay Home", True, (255, 255, 0))
    screen.blit(over_text, (180, 250))

# Game loop
running = True
while running:
    # Background
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left and fire
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #Player movement & boundaries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >=736:
        playerX = 736

    #Enemy movement & boundaries
    for i in range(num_of_enemies):
        # Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736: 
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            bulletY = 500
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        # Calling enemy
        enemy(enemyX[i], enemyY[i], i)
    

    #Bullet movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Calling player
    player(playerX, playerY)

    # Score
    show_score(textX, textY)

    pygame.display.update()

