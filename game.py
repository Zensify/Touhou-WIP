import pygame
from character import *
from setup import *

pygame.init()
fps = 120
clock = pygame.time.Clock()

# Create some character objects
marisa = Character(620, 250, 25, 25)
shoot = Character(1, 1, 5, 5)

# -------- Main Program Loop -----------
loop = True
while loop:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # LOGIC
    marisa.movement(1.5, 1.2)

    # DRAW
    game_window.fill(BLACK)

    marisa.draw()
    shoot.draw()

    pygame.display.flip()

pygame.quit()
