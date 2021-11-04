import pygame, random
from setup import *

class Enemies(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.health = 1
        self.score = 75
             
    def Enemy_movement(self, dx, dy, vel):
        self.dx = dx
        self.dy = dy
        self.vel = vel

    def draw(self):
        pygame.draw.rect(game_window, WHITE, [self.x, self.y, self.w, self.h])
    
    def __str__(self):
        return f"Enemy at [{self.x}, {self.y}]"