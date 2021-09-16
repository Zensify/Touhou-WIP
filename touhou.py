import pygame, sys, random

# Setup
pygame.init()

# Window Settings
window_height = 650
window_width = 800
fps = 120
clock = pygame.time.Clock()

# Colours
color_white = (255, 255, 255)
color_black = (0, 0, 0)

# Window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Touhou Scarlet Devil')

class StartingMenu():
    def __init__(self):
        self.image = pygame.Surface((100, 100))
        self.title = [
            ["Play" (150, 250, 300), self.menu, self.difficultymenu],
            ["Quit" (150, 250, 300), sys.exit]]
        self.difficultymenu = [
            ["Difficulty Settings" (150, 250, 300)],
            ["Easy" (150, 250, 300), self.setdifficulty],
            ["Medium" (150, 250, 300), self.setdifficulty],
            ["Hard" (150, 250, 300), self.setdifficulty]]
        self.level = [
            ["Continue" (150, 250, 300), self.play],
            ["Exit" (150, 250, 300), self.menu, self.title]] 

    def setdifficulty(self, choice):
        self.setdifficulty = choice

    def menu(self):
        font = pygame.font.Font(None, 100)
        self.text = font
        self.menu(self.title)
    
class Vitals():
    def variables(self):
        self.dy = 0
        self.dx = 0
        self.lives = 0
        self.score = 0 

    def movement(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.dy = -3
        if keystate[pygame.K_DOWN]:
            self.dy= 3
        if keystate[pygame.K_LEFT]:
            self.dy= 3
        if keystate[pygame.K_RIGHT]:
            self.dy= 3
        self.character.y += self.dy


# -------- Main Program Loop -----------
while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_window.fill(color_black)


    pygame.display.flip()
