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
        self.font = pygame.font.SysFont(None, 30)
        score_text = self.font.render(str(self.score), True, WHITE, BLACK)
        score_heading = self.font.render("Score Points : ", True, WHITE, BLACK )
        game_window.blit(score_heading, (WINDOW_WIDTH - 230, WINDOW_HEIGHT / 8))
        game_window.blit(score_text, (WINDOW_WIDTH - 80, WINDOW_HEIGHT / 8))


