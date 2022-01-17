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
        self.yspeed = 2

    def enMove(self):
        self.x += 1
        self.yspeed += -0.01
        self.y += self.yspeed

    def draw(self):
        pygame.draw.rect(game_window, WHITE, [self.x, self.y, self.w, self.h])

    def __str__(self):
        return f"Enemy at [{self.x}, {self.y}]"
