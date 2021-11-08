import pygame
from setup import *
from character import *
from enemies import Enemies
from bullet import *

pygame.init()
fps = 60
cooldown = 0
clock = pygame.time.Clock()
marisa = Character(280, 550, 25, 25)
IceFairy = Enemies(280, 75, 25, 25)

bullets = []
enemies = []


def main():
    global cooldown
    # -------- Main Program Loop -----------
    loop = True
    while loop:
        clock.tick(fps)
        loop = game_event()
        game_logic()
        game_draw()

        if cooldown != 0:
            cooldown += -1

        pygame.display.flip()
    pygame.quit()


def game_event():
    global cooldown
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_z] and cooldown == 0:
        bullets.append(Bullet(marisa.x, marisa.y - 35))
        cooldown = 20
    return True


def game_logic():
    marisa.move(2, 1.8)
    for i in range(len(bullets) - 1, -1, -1):
        bullets[i].bullet_move()
        if bullets[i].y < 30:
            bullets.pop(i)


def game_draw():
    game_window.fill(BLACK)
    game_window.blit(background, (50, 35))
    pygame.draw.rect(game_window, WHITE, pygame.Rect(50, 30, 5,
                                                     570))  # Right Line
    pygame.draw.rect(game_window, WHITE, pygame.Rect(550, 30, 5,
                                                     570))  # Left Line
    pygame.draw.rect(game_window, WHITE, pygame.Rect(50, 30, 500,
                                                     5))  # Top Line
    pygame.draw.rect(game_window, WHITE, pygame.Rect(50, 600, 505,
                                                     5))  # Bottom Line
    marisa.draw()
    IceFairy.draw()
    for bullet in bullets:
        bullet.draw()


main()
