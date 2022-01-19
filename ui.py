import pygame
from setup import *

class SideBar():
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.health = 1

    def draw(self):
        font = pygame.font.SysFont(None, 30)

        # ========================= Setup ==================================
        score_text = font.render(str(self.score), True, WHITE, BLACK)
        score_heading = font.render("Score : ", True, WHITE, BLACK)

        lives_text = font.render(str(self.lives), True, WHITE, BLACK)
        lives_heading = font.render("Lives : ", True, WHITE, BLACK)

        health_text = font.render(str(self.health), True, WHITE, BLACK)
        health_heading = font.render("Health : ", True, WHITE, BLACK)
        # ==================================================================

        # ====================== Draw Sidebar Items ===============================
        game_window.blit(score_heading, (WINDOW_WIDTH - 230, WINDOW_HEIGHT / 13))
        game_window.blit(score_text, (WINDOW_WIDTH - 155, WINDOW_HEIGHT / 13))

        game_window.blit(lives_heading, (WINDOW_WIDTH - 230, WINDOW_HEIGHT / 8))
        game_window.blit(lives_text, (WINDOW_WIDTH - 155, WINDOW_HEIGHT / 8))

        game_window.blit(health_heading, (WINDOW_WIDTH - 230, WINDOW_HEIGHT / 5.8))
        game_window.blit(health_text, (WINDOW_WIDTH - 145, WINDOW_HEIGHT / 5.8))
        # =========================================================================

def menuScreen():
    menuFont = pygame.font.SysFont(None, 30)
    menu_heading = menuFont.render("Play", True, BLACK, None)
    
    # Logic
    mx, my = pygame.mouse.get_pos()
    playBtn = pygame.Rect(650, 260, 30, 40)
    if playBtn.collidepoint(mx, my):
        return "play"
    else:
        # Draw
        game_window.fill(BLACK)
        game_window.blit(menuImage, (0, 0))
        #pygame.draw.rect(game_window, (0, 0, 0), playBtn)
        game_window.blit(menu_heading, (650, 260, 30, 40))
        return "menu"