import pygame
from setup import *
from bullet import *
from ui import *


class Enemy_1(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.health = 1
        self.damage = 1
        self.score = 25
        self.ySpeed = 0.015
        #enHitbox = pygame.Rect(self.x, self.y, self.w, self.h)

    def enMove(self):
        self.x += 0.015
        self.ySpeed += -0.00000045
        self.y += self.ySpeed

    def enDraw(self):
        pygame.draw.rect(game_window, WHITE, [self.x, self.y, self.w, self.h])

    def __str__(self):
        return f"Enemy at [{self.x}, {self.y}]"