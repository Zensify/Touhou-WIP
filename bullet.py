import pygame
from setup import *

class Bullet(object):
    def __init__(self, x, y):
        self.image = pygame.image.load("assets\marisa\GreenBullet1.png")
        self.vel = -5
        self.x = x
        self.y = y

    def Bullet_move(self):
        self.y += self.vel

        # Make a Remove Function for Bullets list
        if self.y < 30:
            self.y = 1000
            self.vel = 0

    def draw(self):
        game_window.blit(self.image, (self.x, self.y))
