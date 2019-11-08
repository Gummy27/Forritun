import pygame
from random import randint

pygame.init()
pygame.font.init()
class Dice():
    def __init__(self, face):
        self.sprite = pygame.image.load('sd'+str(face)+'.png')
        self.face = face

    def throw(self, play=False):
        if play:
            self.face = 0
        else:
            self.face = randint(1, 6)
        self.sprite = pygame.image.load('sd'+str(self.face)+'.png')

class Die():
    def __init__(self):
        self.win = False
        die, dieB = [], []
        for i in range(2):
            for x in range(5):
                dieB.append(Dice(0))
            die.append(dieB)
            dieB = []
        self.die = die

    def throwDie(self, play=False):
        print("yes")
        for x, player in enumerate(self.die):
            for y, dice in enumerate(player):
                if x != 1 and y != 5:
                    dice.throw()
                elif play:
                    dice.throw()
        pygame.display.update()

    def drawGraphics(self):
        for y, player in enumerate(self.die):
            for x, dice in enumerate(player):
                print(y, x)
                if y == 1 and x == 4:
                    if self.win:
                        win.blit(dice.sprite, (x*100+5, y*100+50))
                    else:
                        win.blit(pygame.image.load('sd0.png'), (x*100+5, y*100+50))
                else:
                    win.blit(dice.sprite, (x * 100 + 5, y * 100 + 50))

win = pygame.display.set_mode((500, 500))
active = Die()

myfont = pygame.font.SysFont('Comic Sans MS', 60)

# 500 - 40: 460

cords, hitbox = 0, []
messeges = ['Play', 'All', 'One']
for index, messege in enumerate(messeges):
    pygame.draw.rect(win, ([255, 255, 255]), [50 + cords, 300, 100, 50], 0)
    text = myfont.render(messege, False, (0, 0, 0))
    win.blit(text, (50 + cords, 300))
    hitbox.append([[50 + cords, 300], [50 + cords + 100, 350]])
    cords += 150

active.drawGraphics()
pygame.display.update()

hovering = 3
running = True
holding = False
while running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        active.throwDie()
        active.drawGraphics()
        pygame.display.update()

    mpos = pygame.mouse.get_pos()
    # [[50, 300], [150, 50]]
    for index, cords in enumerate(hitbox):
        x1 = cords[0][0]
        x2 = cords[1][0]
        y1 = cords[0][1]
        y2 = cords[1][1]
        if x2 > mpos[0] > x1 and y2 > mpos[1] > y1:
            if hovering == 3:
                pygame.draw.rect(win, ([0, 255, 255]), [x1, y1, 100, 50], 0)
                text = myfont.render(messeges[index], False, (0, 0, 0))
                win.blit(text, (x1, y1))
                pygame.display.update()
                hovering = index
        elif hovering != 3 and hovering == index:
            cords = hitbox[hovering]
            x1 = cords[0][0]
            x2 = cords[1][0]
            y1 = cords[0][1]
            y2 = cords[1][1]
            pygame.draw.rect(win, ([255, 255, 255]), [x1, y1, 100, 50], 0)
            text = myfont.render(messeges[index], False, (0, 0, 0))
            win.blit(text, (x1, y1))
            pygame.display.update()
            hovering = 3

    click = pygame.mouse.get_pressed()[0]
    if click and not holding:
        holding = True
        for index, cords in enumerate(hitbox):
            x1 = cords[0][0]
            x2 = cords[1][0]
            y1 = cords[0][1]
            y2 = cords[1][1]
            if x2 > mpos[0] > x1 and y2 > mpos[1] > y1:
                # Spila
                if index == 0:
                    active.throwDie()
                # All
                elif index == 1:
                    pass
                # One
                elif index == 2:
                    pass




