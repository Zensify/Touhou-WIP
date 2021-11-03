import pygame
from setup import *


class Character(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def movement(self, x, y):
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
        if self.y < 0:
            self.y = 0
        elif self.y > 625:
            self.y = 625
        if self.x > 775:
            self.x = 775
        elif self.x < 0:
            self.x = 0

    def draw(self):
        pygame.draw.rect(game_window, WHITE, [self.x, self.y, self.w, self.h])

    def __str__(self):
        return f"Character at [{self.x}, {self.y}]"


class Bullet(object):
    def __init__(self, x, y):
        self.image = pygame.image.load("assets\marisa\GreenBullet1.png")
        self.rect = self.image.get_rect()
        self.vel = -5
        self.x = x
        self.y = y

    def move(self):
        self.y += self.vel

    def draw(self):
        game_window.blit(self.image, (self.x, self.y))
