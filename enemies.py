from multiprocessing.connection import wait
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

    def move(self, velocity):
        if self.y <= 324 and self.x <= 324:
            self.y += 2 
            self.x += 1
            velocity += self.x

        elif self.y >= 325 and self.x >= 325:
            self.y -= 3
            self.x += 4
            velocity += self.x


    def draw(self):
        pygame.draw.rect(game_window, WHITE, [self.x, self.y, self.w, self.h])

    def __str__(self):
        return f"Enemy at [{self.x}, {self.y}]"


# ---  Movement ---
    # - Sine Curve
    # - Fly down then fly Right/Left
