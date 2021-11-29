import pygame
from setup import *


class Character(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.health = 1
        self.lives = 3
        self.damage = 1

    def move(self, x, y):
        self.dy = 0
        self.dx = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.dy = -y
        elif keystate[pygame.K_s]:
            self.dy = y
        if keystate[pygame.K_a]:
            self.dx = -x
        elif keystate[pygame.K_d]:
            self.dx = x
        self.y += self.dy
        self.x += self.dx

        # Clamp Player To Screen
        if self.y < 30:
            self.y = 30
        elif self.y > 575:
            self.y = 575
        if self.x > 525:
            self.x = 525
        elif self.x < 50:
            self.x = 50

    def draw(self):
        pygame.draw.rect(game_window, WHITE, [self.x, self.y, self.w, self.h])

    def __str__(self):
        return f"Character at [{self.x}, {self.y}]"
