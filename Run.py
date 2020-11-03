import sys

import pygame
pygame.init()

width = 500
height = 350
screen = pygame.display.set_mode((width, height))
speed = [2, 2]
red = 255, 0, 0

Enemy = pygame.image.load("Enemy.png")
Enemy_rect = Enemy.get_rect()

# Anything that you want to be persistent has to go inside the while loop (i.e. images, text).
running = True
while running:

  # listen for events
  for event in pygame.event.get():
    # terminate game on exit
    if event.type == pygame.QUIT:
      sys.exit()
  # update sprite location
  Enemy_rect = Enemy_rect.move(speed)
  if Enemy_rect.left < 0 or Enemy_rect.right > width:
    speed[0] = -speed[0]
  if Enemy_rect.top < 0 or Enemy_rect.bottom > height:
    speed[1] = -speed[1]
  # repaint the screen
  screen.fill(red)
  screen.blit(Enemy, Enemy_rect)
  pygame.display.flip()