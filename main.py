import pygame
from setup import *
from character import *
from enemies import *
from bullet import *
from ui import *


pygame.init()
fps = 60
cooldown = 0
clock = pygame.time.Clock()
marisa = Character(280, 550, 25, 25)
iceFairy = Enemy_1(280, 30, 25, 25)
bullets = []
enemies = []

sideBar = SideBar()


def main():
    global cooldown
    level = "menu"

    # -------- Main Program Loop -----------
    loop = True
    while loop:
        clock.tick(fps)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # Check Level
        if level == 'menu':
            level = menuScreen()
        elif level == 'play':
            game_event()
            game_logic()
            game_draw()

        pygame.display.flip()
    pygame.quit()


def game_event():
    global cooldown
    enemies.append(iceFairy)

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_z] and cooldown == 0:
        bullets.append(Bullet(marisa.x, marisa.y - 35))
        cooldown = 20  # --- bullets can only be shot every 20 frames


def game_logic():
    global cooldown
    marisa.move(2.5, 2.8)

    if cooldown != 0:
        cooldown += -1

    for i in range(len(bullets) - 1, -1, -1):
        bullets[i].bullet_move()
        if bullets[i].y < 30:
            bullets.pop(i)

    for i in range(len(enemies) - 1, -1, -1):
        enemies[i].enMove()
        if (enemies[i].y > 30) and (enemies[i].x > 530):
            enemies.pop(i)

    for i in range(len(enemies) - 1, -1, -1):
        enHitbox = pygame.Rect(enemies[i].x, enemies[i].y, 25, 25)

        if enemies[i].health == 0:
            enemies.pop(i)

        for j in range(len(bullets) - 1, -1, -1):
            bulletHitbox = pygame.Rect(bullets[j].x, bullets[j].y, 25, 25)

            if pygame.Rect.colliderect(enHitbox, bulletHitbox):
                iceFairy.health -= marisa.damage
                sideBar.score += iceFairy.score
                bullets.pop(j)


def game_draw():
    game_window.fill(BLACK)
    #game_window.blit(background, (50, 35))
    sideBar.draw()
    marisa.draw()

    for enemy in enemies:
        enemy.enDraw()

    for bullet in bullets:
        bullet.draw()

    # ===================== Play Area ================================
    pygame.draw.rect(game_window, WHITE, pygame.Rect(50, 30, 500, 5))   # Top Line
    pygame.draw.rect(game_window, WHITE, pygame.Rect(50, 30, 5, 570))   # Left Line
    pygame.draw.rect(game_window, WHITE, pygame.Rect(550, 30, 5, 570))  # Right Line
    pygame.draw.rect(game_window, WHITE, pygame.Rect(50, 600, 505, 5))  # Bottom Line
    # =================================================================
    
    # ======================= Side Bar ================================
    pygame.draw.rect(game_window, WHITE, pygame.Rect(560, 35, 185, 5))  # Top Line
    pygame.draw.rect(game_window, WHITE, pygame.Rect(740, 35, 5, 110))  # Left Line
    pygame.draw.rect(game_window, WHITE, pygame.Rect(560, 35, 5, 110))  # Right Line
    pygame.draw.rect(game_window, WHITE, pygame.Rect(560, 140, 185, 5)) # Bottom Line
    # =================================================================

main()
