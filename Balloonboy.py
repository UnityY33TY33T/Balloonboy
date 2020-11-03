import sys
import pygame
from pygame import mixer
pygame.init()
# size of the playing screen
screen_width = 1250
screen_height = 840
screen = pygame.display.set_mode((screen_width, screen_height))
# Player
Playerleft = pygame.image.load('Balloon.png')
Playerright = pygame.image.load('Playerright.png')
Playerleft_rect = Playerleft.get_rect()
Playerright_rect = Playerright.get_rect()
# Background
bg = pygame.image.load('Background.jpg')
# color of playing screen
blue = 0, 0, 205
# position of the sprite
x = 500
y = 500
# size of the player
width = 64
height = 64
# speed of player
vel = 33
# Enemy speed
speed = [1, 1]
# player's abilities to jump variables
Is_jump = False
jumpCount = 10
# Drawing and animations
screen.fill(blue)
screen.blit(Playerleft, Playerleft_rect)
screen.blit(Playerright, Playerright_rect)
# Time frames
clock = pygame.time.Clock()
class Enemy(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = (self.x, (self.end))
        self.walkCount = 0
        self.vel = 5
    def draw(self, screen):
        pass
    def move(self):
        pass
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 30
        self.Is_jump = False
        self.jumpCount = 10
        self.right = False
        self.left = False
        self.walkCount = 0
def redrawGameWindow():
    global walkCount
    screen.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        screen.blit(Playerleft, (x, y))
        walkCount += 1
    elif right:
        screen.blit(Playerright, (x, y))
        walkCount += 1
    else:
        screen.blit(Playerright, (x, y))
        walkCount = 0
    pygame.display.update()
# mainloop
MD = Player(300, 410, 64, 64)
run = True
while 1:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= MD.vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_width - width - vel:
        x += MD.vel
        right = True
        left = False
    elif keys[pygame.K_UP] and y > vel:
        y -= vel
    elif keys[pygame.K_DOWN] and y < screen_height - height - vel:
        y += vel
    else:
        right = False
        left = False
        walkCount = 0
    if not Is_jump:
        if keys[pygame.K_SPACE] and y > vel:
            Is_jump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            Is_jump = False
            jumpCount = 10
    Enemy = pygame.image.load("Enemy.png")
    Enemy_rect = Enemy.get_rect()
    Enemy_rect = Enemy_rect.move(speed)
    if Enemy_rect.left < 0 or Enemy_rect.right > screen_width:
        speed[0] = -speed[0]
    if Enemy_rect.top < 0 or Enemy_rect.bottom > screen_height:
        speed[1] = -speed[1]
    screen.blit(Enemy, Enemy_rect)
    pygame.display.flip()
    redrawGameWindow()
pygame.quit()
