import pygame
from character import *
from setup import *

bullets = []


class Marisa():
    def __init__(self):
        self.health = 1
        self.lives = 3
        self.damage = 5

    def update():
        marisa = Character(400, 580, 25, 25)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_z]:
            bullets.append(Bullet(marisa.x, marisa.y - 35))

        marisa.move(2, 1.2)
        for bullet in bullets:
            bullet.move()

        marisa.draw()
        for bullet in bullets:
            bullet.draw()