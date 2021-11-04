import pygame
from pygame import display
import random


#init pygame
pygame.init()


#create screen (800x600 resolution)
screen=pygame.display.set_mode((800,600))

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

def player(x,y):
    screen.blit(playerimage,(x,y))

#Enemy alien 1
alien1=pygame.image.load('alien1.png')
alien1imageX = random.randint (0,800)
alien1imageY = random.randint (50,150)
alien1imageXchange = 1
alien1imageYchange = 40

def enemy1(x,y):
    screen.blit(alien1, (x,y))




#Game Loop

running = True

while running:
    screen.fill((70,70,70))  #(red, green, blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if key is pressed, check whether it is right or left arrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerimageXchange = -3
            if event.key == pygame.K_RIGHT:
                playerimageXchange = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerimageXchange = 0

    # check for out of bounds for player
    playerimageX += playerimageXchange
    if playerimageX > 736:
        playerimageX = 736
    if playerimageX < 0:
        playerimageX = 0

    #check for out of bounds for player
    alien1imageX += alien1imageXchange
    if alien1imageX > 736:
        alien1imageXchange = -1 * alien1imageXchange
        alien1imageY += alien1imageYchange
    if alien1imageX < 0:
        alien1imageXchange = -1 * alien1imageXchange
        alien1imageY += alien1imageYchange
        

    

    player(playerimageX, playerimageY)
    enemy1(alien1imageX,alien1imageY)
    pygame.display.update()

    

