import pygame
from pygame.locals import *
from random import randint

pygame.init()

rock_color = (0,0,0)

W, H = 800, 600
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Penetrator')

fps = 27
probability = 100
missile_speed = 3

bgUp = []
bgDown = []
minPassage = 200
maxPassage = 300
enemy = []

def FirstborderGenerator():
    for i in range(20):
        bgUp.append(20)
        bgDown.append(H-20)
        enemy.append(0)
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
    y = randint(0,100)
    if b+x>H-20:
        pos = H-20
    elif b+x<a+minPassage:
        pos = a+minPassage
    else:
        pos = b+x
    bgDown.append(pos)

    y = randint(0,1000)
    if y>1000 - probability:
        enemy.append(pos)
    else:
        enemy.append(0)


def collision():
    col = False
    if abs(playerY-bgUp[playerX//10])<radius or abs(playerY-bgDown[playerX//10])<radius:
        col =  True
    for i in range(len(enemy)-20):
        if (enemy[i]-playerY)**2+(i*10-playerX)**2<(radius+10)**2:
            col = True
    return col

def redrawWindow():
    win.fill((255,255,255))
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
    pygame.draw.polygon(win, (rock_color), temenaUp)
    pygame.draw.polygon(win, (rock_color), temenaDown)
    pygame.draw.circle(win, pygame.Color("green"), (playerX, playerY), radius)
    for i in range(len(enemy)):
        if enemy[i]!=0:
            pygame.draw.polygon(win,pygame.Color("red"), ((i*10, enemy[i]),(i*10+5, enemy[i]+5),(i*10, enemy[i]-10),(i*10-5, enemy[i]+5)))

    font = pygame.font.SysFont("Arial", 50)
    tekst = font.render(str(counter), True, pygame.Color("yellow"))
    win.blit(tekst, (0, 0))
    pygame.display.update()



run = True

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
    clock.tick(fps)

    bgUp = bgUp[1:]
    bgDown = bgDown[1:]
    enemy = enemy[1:]
    BorderGenerator(bgUp[-1], bgDown[-1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                dy = -10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                dy = 10
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                dx = -10
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                dx = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                dy = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                dy = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                dx = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                dx = 0

    playerX += dx
    if playerX>(W*3)//4:
        playerX = (W*3)//4
        dx = 0
    if playerX<(W*1)//8:
        playerX = (W*1)//8
        dx = 0
    playerY += dy

    for i in range(len(enemy)):
        if enemy[i]!=0:
            enemy[i] -= missile_speed

    redrawWindow()

    if collision():
        run = False
        print(counter)
