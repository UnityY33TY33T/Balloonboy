import pygame
from pygame import mixer

width = 800
height = 600

Player = pygame.image.load('Playerright.png')
Enemy = pygame.image.load('Skull.png')
Enemy_rect = Enemy.get_rect()


x = 400
y = 550

speed = 1

balloonX_change = 0

balloonY_change = 0
screen = pygame.display.set_mode((width, height))
def player(x, y):
    screen.blit(Player, (x, y))

running = True
while running:

    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                balloonX_change = -1
            if event.key == pygame.K_RIGHT:
                balloonX_change = 1
            if event.key == pygame.K_UP:
                balloonY_change = -1
            if event.key == pygame.K_DOWN:
                balloonY_change = 1

    x += balloonX_change
    if x <= 0:
        balloonX = 0
    if x >= 770:
        x = 770
    y += balloonY_change
    if y <= 0:
        y = 0
    elif y >= 570:
        y = 570
    player(x, y)



if Enemy_rect.left < 0 or Enemy_rect.right > width:
               speed[0] = -speed[0]
if Enemy_rect.top < 0 or Enemy_rect.bottom > height:
               speed[1] = -speed[1]

screen.blit(Enemy, Enemy_rect)
pygame.display.flip()

pygame.display.update()
