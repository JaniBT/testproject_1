import random
import sys
import pygame

BLACK = 0, 0, 0
WHITE = 255, 255, 255
WIDTH = 600
HEIGHT = 400
clock = pygame.time.Clock()

#Alap program
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

player_x = 280
player_y = 360
player = pygame.Rect(player_x, player_y, 20, 10)


status = True
while status:
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
            sys.exit()

        key = pygame.key.get_pressed()
        if player_x < 580 or player_x > 20:
            if key[pygame.K_RIGHT]:
                player_x += 5
            if key[pygame.K_LEFT]:
                player_x -= 5
    

    pygame.display.update()
    clock.tick(60)

pygame.quit()