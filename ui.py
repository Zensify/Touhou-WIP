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
        return "menu"

class SideBar():
    def __init__(self):
        self.highscore = 0
        self.score = 0
        self.lives = 3
        self.health_points = 1

    def draw(self):
        self.font = pygame.font.SysFont(None, 50)
        self.score = self.font.render(str(self.score), True, WHITE, BLACK)
        game_window.blit(self.score, (WINDOW_WIDTH - 45, WINDOW_HEIGHT / 8))


