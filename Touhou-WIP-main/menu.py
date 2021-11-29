import pygame
from setup import *

def menuScreen():
    # Logic
    mx, my = pygame.mouse.get_pos()
    playBtn = pygame.Rect(570, 260, 150, 20)
    if playBtn.collidepoint(mx, my):
        return "play"
    else:
        # Draw
        game_window.fill(BLACK)
        game_window.blit(menuImage, (0, 0))
        pygame.draw.rect(game_window, (0, 0, 0), playBtn)
        return "menu";

