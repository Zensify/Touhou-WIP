import pygame
from setup import *


class Bullet(object):
    def __init__(self, x, y):
        self.image = pygame.image.load("assets\marisa\Bullet.png")
        self.vel = -5
        self.x = x
        self.y = y

    def bullet_move(self):
        self.y += self.vel

    def draw(self):
        game_window.blit(self.image, (self.x, self.y))
