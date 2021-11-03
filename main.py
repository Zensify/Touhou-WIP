import pygame
from setup import *
from game import *

pygame.init()
fps = 60
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
loop = True
while loop:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # DRAW
    game_window.fill(BLACK)

    Marisa.update()

    pygame.display.flip()
pygame.quit()