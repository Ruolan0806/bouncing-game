import pygame
import sys

pygame.init()
size= width, height=400,600
bg=(255,255,255)
speed= [-2,1]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("The first game")
animal=pygame.image.load("animal.JPG")
position=animal.get_rect()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
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




