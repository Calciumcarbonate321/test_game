import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("GG")

#Icon and name
icon = pygame.image.load('trophy.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('background.png')

#Player
playerImg= pygame.image.load('aircraft.png')
playerX= 400
playerY= 500
normalXspeed= 0
normalYspeed= 0

#enemy
enemyImg= pygame.image.load('enemy.png')
enemyX= random.randint(10,700)
enemyY= random.randint(0,200)
enemyXspeed= 2
enemyYspeed= 0

def player(x,y):
    screen.blit(playerImg,(x, y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

running = True

while running:
    screen.fill((100, 100, 100))           #Colour
    screen.blit(bg, (0, 0))                #background

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        #Player controls
        if event.type==pygame.KEYDOWN:     
            if event.key==pygame.K_LEFT:
               normalXspeed= -2
            if event.key==pygame.K_RIGHT:
               normalXspeed= 2
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                normalXspeed= 0

    #Player movement
    playerY+= normalYspeed
    playerX+= normalXspeed
    if playerX<= 0:
        playerX=0
    elif playerX>=778:
        playerX=778
    elif playerY<=32:
        playerY=32
    elif playerY>=568:
        playerY=568

    #Enemy movement
    enemyX+=enemyXspeed
    if enemyX<= 0:
        enemyXspeed= random.randrange(1,2)
    elif enemyX>=768:
        enemyXspeed= random.randrange(-2,-1)
    elif enemyY>=32:
        enemyYspeed=0.3
    enemyY+=enemyYspeed

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
    