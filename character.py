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

    #def bullets(self, x, y, dx, dy):
        #self.x = y
        #self.y = x
        #self.dx = dy
        #self.dy = dx

        #bullet = []
        #shoot = bullet(self.x, self.y, self.dx, self.dy)

        #keystate = pygame.key.get_pressed()
        #if keystate[pygame.K_z]

    def draw(self):
        pygame.draw.rect(game_window, WHITE, [self.x, self.y, self.w, self.h])
        pygame.draw.rect(game_window, RED, [self.x, self.y, self.w, self.h])

    def __str__(self):
        return f"Character at [{self.x}, {self.y}]"
