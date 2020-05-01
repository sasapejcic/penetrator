import pygame
from pygame.locals import *
from random import randint

pygame.init()

W, H = 800, 600
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Penetrator')

bgUp = []
bgDown = []
minPassage = 200
maxPassage = 300

def FirstborderGenerator():
    for i in range(20):
        bgUp.append(20)
        bgDown.append(H-20)
    for i in range(20,80):
        BorderGenerator(bgUp[-1], bgDown[-1])

def BorderGenerator(a, b):
    x = randint(-50, 50)
    if a+x<20:
        bgUp.append(20)
    elif a+x>b-minPassage:
        bgUp.append(b-minPassage)
    else:
        bgUp.append(a+x)

    x = randint(-50, 50)
    if b+x>H-20:
        bgDown.append(H-20)
    elif b+x<a+minPassage:
            bgDown.append(a+minPassage)
    else:
        bgDown.append(b+x)

def collision():
    if abs(playerY-bgUp[playerX//10])<radius or abs(playerY-bgDown[playerX//10])<radius:
        return True
    else:
        return False


def redrawWindow():
    win.fill((0,0,0))
    temenaUp = []
    temenaDown = []
    for i in range(len(bgUp)):
        temenaUp.append((i*10, bgUp[i]))
        temenaDown.append((i*10, bgDown[i]))
    temenaUp.append((W,bgUp[-1]))
    temenaUp.append((W,0))
    temenaUp.append((0,0))
    temenaDown.append((W,bgDown[-1]))
    temenaDown.append((W,H))
    temenaDown.append((0,H))
    pygame.draw.polygon(win, pygame.Color("white"), temenaUp, 5)
    pygame.draw.polygon(win, pygame.Color("white"), temenaDown, 5)
    pygame.draw.circle(win, pygame.Color("green"), (playerX, playerY), radius)

    font = pygame.font.SysFont("Arial", 20)
    tekst = font.render(str(counter), True, pygame.Color("yellow"))
    win.blit(tekst, (0, 0))
    pygame.display.update()

run = True
speed = 30
counter = 0

playerX = W//4
playerY = H//2
dx = 0
dy = 0
radius = 20

clock = pygame.time.Clock()

FirstborderGenerator()

while run:
    counter +=1
    clock.tick(speed)

    bgUp = bgUp[1:]
    bgDown = bgDown[1:]
    BorderGenerator(bgUp[-1], bgDown[-1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                dy = -10
            if event.key == pygame.K_DOWN:
                dy = 10
            if event.key == pygame.K_LEFT:
                dx = -10
            if event.key == pygame.K_RIGHT:
                dx = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                dy = 0
            if event.key == pygame.K_DOWN:
                dy = 0
            if event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_RIGHT:
                dx = 0

    playerX += dx
    if playerX>(W*3)//4:
        playerX = (W*3)//4
        dx = 0
    playerY += dy

    if collision():
        run = False

    redrawWindow()
