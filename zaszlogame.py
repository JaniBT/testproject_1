import pygame
import os
import random
import sys


WIDTH = 600
HEIGHT = 400
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREENISH = 0, 225, 0


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flag Guesser")

    def zaszlok():
        au = pygame.image.load("./zaszlok/w320/au.png").convert()
        screen.blit(au, 250, 150, 50)
    
    zaszlok()



    state = True

    while state:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False
                sys.exit(0)
        
        screen.blit(zaszlok(), (250, 150), 50)
        
        pygame.display.update()
        
    pygame.quit()

main()