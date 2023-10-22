import random, pygame, time, os, sys

MAGASSAG = 700
SZELESSEG = 500
ZOLD = 0, 255, 0
PIROS = 255, 0, 0
FEKETE = 0, 0, 0
SARGA = 254, 225, 43
FEHER = 255, 255, 255

kigyox = 50
kigyoy = 20

pygame.init()

kepernyo = pygame.display.set_mode((MAGASSAG, SZELESSEG))
pygame.display.set_caption("Snake Game by Jani")
kigyo = pygame.Rect(kigyox, kigyoy, 20, 20)

statusz = True
while statusz:
    pygame.display.flip()
    kepernyo.fill(FEHER)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            statusz = False
            sys.exit()
    
    gombok = pygame.key.get_pressed()
    if gombok[pygame.K_w]:
        kigyoy += 10
    if gombok[pygame.K_s]:
        kigyoy -= 10
    if gombok[pygame.K_a]:
        kigyox -= 10
    if gombok[pygame.K_d]:
        kigyox += 10
    
    pygame.draw.rect(kepernyo, ZOLD, kigyo, 20)
    
    pygame.display.update()

pygame.quit()