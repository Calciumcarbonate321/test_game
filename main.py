import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("GG")

#Icon and name
icon = pygame.image.load('trophy.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('background.png')


#Speeds
normalXspeed= 0
normalYspeed= 0

bulletXspeed= 0
bulletYspeed= 6


class Bullet:
    Img = pygame.image.load('bullet.png')

    def __init__(self, X, Y):
        self.X = X-2
        self.Y = Y


class Player:
    Img = pygame.image.load('aircraft.png')

    X = 400
    Y = 500
    

class Enemy:
    Img = pygame.image.load('enemy.png')
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    Xspeed= 2
    Yspeed= 0


bullets = []
enemies = []
enemy_lvl = 0
score = 0
font = pygame.font.Font('freesansbold.ttf', 10)


running = True


while running:
    screen.fill((100, 100, 100))           #Colour
    screen.blit(bg, (0, 0))                #background

    text = font.render(f'Score: {score}', True, (255, 255, 255), (0, 0, 0))   #ScoreText
    textRect = text.get_rect()
    textRect.center = (30, 10)
    screen.blit(text, textRect)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        #Player controls
        if event.type==pygame.KEYDOWN:     
            if event.key==pygame.K_LEFT:
               normalXspeed= -2
            if event.key==pygame.K_RIGHT:
               normalXspeed= 2
            if event.key==pygame.K_SPACE:
                bullets.append(Bullet(Player.X, Player.Y))
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                normalXspeed= 0

    #new enemies
    if len(enemies) == 0:
        for i in range(enemy_lvl := enemy_lvl+1):
            enemies.append(Enemy(random.randint(10,700), random.randint(0,200)))
        

    #Player movement
    Player.Y+= normalYspeed
    Player.X+= normalXspeed
    if Player.X<= 0:
        Player.X=0
    elif Player.X>=778:
        Player.X=778
    elif Player.Y<=32:
        Player.Y=32
    elif Player.Y>=568:    
        Player.Y=568


    screen.blit(Player.Img, (Player.X, Player.Y))


    #Enemy movement
    for i in enemies:
        i.X+=i.Xspeed
        if i.X<= 0:
            i.Xspeed= random.randrange(1,2)
        elif i.X>=768:
            i.Xspeed= random.randrange(-2,-1)
        elif i.Y>=32:
            i.Yspeed=0.3
        i.Y+=i.Yspeed
        screen.blit(i.Img, (i.X, i.Y))


    #Bullet movement
    for i in bullets:
        i.Y -= bulletYspeed
        screen.blit(i.Img, (i.X, i.Y))
        if i.Y<0:
            del bullets[bullets.index(i)]
        for j in enemies:
            if (i.Y > j.Y-30 and i.Y < j.Y+30) and (i.X > j.X-30 and i.X < j.X+30):
                del bullets[bullets.index(i)]
                del enemies[enemies.index(j)]
                score+=100
                print("bullet shot on enemy")
    
    pygame.display.update()

    
    