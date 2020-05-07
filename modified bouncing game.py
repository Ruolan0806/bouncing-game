import pygame
import sys
from pygame.locals import *

pygame.init()
size= width, height=400,600
bg=(255,255,255)
speed= [-2,1]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("The first game")
animal=pygame.image.load("animal.JPG")
position=animal.get_rect()
bgm=pygame.mixer.music.load("Love shot.mp3")
pygame.mixer.music.play()
while True:
    #speed = [-2, 1]
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                speed=[-1,0]
            if event.key == K_RIGHT:
                speed = [1, 0]
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]
    position = position.move(speed)
    if position.left < 0 or position.right > width:
        animal=pygame.transform.flip(animal,True,False)
        speed[0]=-speed[0]
    if position.top<0 or position.bottom > height:
        speed[1]=-speed[1]

    screen.fill(bg)
    screen.blit(animal,position)
    pygame.display.flip()
    pygame.time.delay(10)




