from numpy import true_divide
import pygame
from pygame import display
from pygame import mixer
import random
import math
import time

#init pygame
pygame.init()
pygame.mixer.init()

'''CLOCK, FPS, and CLOCK.tick() are my solution to a "speed" problem.  Randomly, the game would 
*significantly* speed up, by 300% or more.  Without knowing exactly how things were rendered/refreshed, 
I threw this fix against the wall, hoping it would stick.  It appears
to have solved the problem.  The game now runs smoothly'''

CLOCK = pygame.time.Clock()
FPS = 60

#create screen (800x600 resolution)
screen=pygame.display.set_mode((800,600))

# background image
background = pygame.image.load('background.jpeg').convert()

#background sound
'''
mixer.music.load('background.wav')
mixer.music.play(-1)
'''

#Ttitle and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('pewpew.png')
pygame.display.set_icon(icon)

#Player
playerimage=pygame.image.load('ship.png')
playerimageX = 370
playerimageY = 480
playerimageXchange = 0
playerimageYchange = 0

#score

score_value = 0
font = pygame.font.Font ('freesansbold.ttf',32)
textX = 10
textY = 10

def show_score (x,y):
    score = font.render ("Score: " + str(score_value),True,(255,255,255))
    screen.blit (score, (x,y))

#game over text

def game_over_text():
    game_over = font.render ("GAME OVER!!!!!!!" ,True,(255,255,255))
    screen.blit (game_over, (200,250))



#Enemy alien 1

alien1=[]
alien1imageX = []
alien1imageY = []
alien1imageXchange = []
alien1imageYchange = []

num_of_enemies = 5

for i in range (num_of_enemies):

    alien1.append(pygame.image.load('alien1.png'))
    alien1imageX.append(random.randint (0,735))
    alien1imageY.append(random.randint (50,150))
    alien1imageXchange.append(random.randint(1,7))
    alien1imageYchange.append(40)




#Bullet
bulletimage=pygame.image.load('bullet.png')
bulletimageX = 0
bulletimageY = 480
bulletimageXchange = 0
bulletimageYchange = 10
bullet_state = "ready"
hit_sound = pygame.mixer.Sound("hugo.wav")
shoot_sound = pygame.mixer.Sound("laser.wav")


def enemy_hit_ship(ypos):
    if ypos >= 450:
        return True
    return False





def player(x,y):
    screen.blit(playerimage,(x,y))



def enemy1(x,y,i):
    screen.blit(alien1[i], (x,y))



def shoot_bullet (x,y):
    global bullet_state
    global bulletimageX
    bullet_state = "fire"
    screen.blit(bulletimage, (x+16,y+10))

def is_collision (enemyX, enemyY, bulletX, bulletY):
       #hit detection
    #dist = ((bulletimageX-alien1imageX)*(bulletimageX-alien1imageX)) + ((bulletimageY-alien1imageY)*(bulletimageY-alien1imageY))
    dist = math.pow(enemyX-bulletX,2)+ math.pow(enemyY-bulletY,2)
    distancebetweenbulletandenemy = math.sqrt (dist)
    if distancebetweenbulletandenemy <27:
        return True
        print (distancebetweenbulletandenemy)
    else:
        return False
        print (distancebetweenbulletandenemy)



#Game Loop

running = True

while running:
    screen.fill((70,70,70))  #(red, green, blue)
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if key is pressed, check whether it is right or left arrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerimageXchange = -3
            if event.key == pygame.K_RIGHT:
                playerimageXchange = 3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletimageX = playerimageX
                    shoot_bullet(bulletimageX,bulletimageY)
                    shoot_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerimageXchange = 0

    # check for out of bounds for player
    playerimageX += playerimageXchange
    if playerimageX > 736:
        playerimageX = 736
    if playerimageX < 0:
        playerimageX = 0

    #check for out of bounds for alien

    for i in range (num_of_enemies):

        #game over situation
        if enemy_hit_ship(alien1imageY[i]):
            print ("DEAD!!!!!!!!!")
            for j in range (num_of_enemies):
                alien1imageY[j] = 2000
            game_over_text()
            break
        

        alien1imageX[i] += alien1imageXchange[i]
        if alien1imageX[i] > 736:
            alien1imageXchange[i] = -1 * alien1imageXchange[i]
            alien1imageY[i] += alien1imageYchange[i]
        if alien1imageX[i] < 0:
            alien1imageXchange[i] = -1 * alien1imageXchange[i]
            alien1imageY[i] += alien1imageYchange[i]
        


        collision = is_collision (alien1imageX[i],alien1imageY[i], bulletimageX, bulletimageY)
        if collision:
            print ("Collision!!!!!")
            bulletimageY = 480
            bullet_state = "ready"
            hit_sound.play()
            score_value += 1
            #print (score)
            alien1imageX[i] = random.randint (0,735)
            alien1imageY[i] = random.randint (50,150)

        enemy1(alien1imageX[i],alien1imageY[i],i)
        

    #bullet movement
    if bulletimageY < 0:
            bullet_state = "ready"
            bulletimageY = 480

    if bullet_state is "fire":
        shoot_bullet(bulletimageX, bulletimageY)
        bulletimageY -= bulletimageYchange


    show_score(textX,textY)
    player(playerimageX, playerimageY)
   
    pygame.display.update()
    CLOCK.tick(FPS)


    

