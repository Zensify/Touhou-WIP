import pygame
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN
from character import *
from setup import *
from menu import *

pygame.init()
fps = 60
clock = pygame.time.Clock()

# Create some character objects
marisa = Character(400, 580, 25, 25)

bullets = []

# -------- Main Program Loop -----------

loop = True
while loop:
    clock.tick(fps)
    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == KEYDOWN:
            if event.key == MOUSEBUTTONDOWN:
                if event.button == 1: 
                    click = True
        if event.type == KEYDOWN:
            if event.key == pygame.K_z:
                bullets.append(Bullet(marisa.x, marisa.y - 35))

    # LOGIC
    marisa.movement(2, 1.2)
    for bullet in bullets:
        bullet.move()

    # DRAW
    #game_window.fill(BLACK)

    marisa.draw()
    for bullet in bullets:
        bullet.draw()

    pygame.display.flip()

pygame.quit()
