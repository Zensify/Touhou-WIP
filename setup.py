import pygame

# -- Window Settings --
WINDOW_HEIGHT = 650
WINDOW_WIDTH = 800

# -- Colours --
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# -- Window --
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Touhou')
background = pygame.image.load(r"Touhou-WIP-main\assets\ui\images.jpg").convert_alpha()
menuImage = pygame.image.load(r"Touhou-WIP-main\assets\ui\mainmenu.png").convert_alpha()