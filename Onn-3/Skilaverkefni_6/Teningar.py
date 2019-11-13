import pygame
from random import randint

pygame.init()
pygame.font.init()

class Dice():
    def __init__(self, face):
        self.sprite = pygame.image.load('sd'+str(face)+'.png')
        self.face = face

    def throw(self, play=False):
        nr = randint(1, 6)
        self.face = nr
        image = 'sd'+str(nr)+'.png'

        self.sprite = pygame.image.load(image)

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

    def throwAllDie(self):
        for x, player in enumerate(self.die):
            for y, dice in enumerate(player):
                dice.throw()
        self.drawGraphics()

    def throwAllPlayer(self):
        for dice in self.die[1]:
            dice.throw()
        self.drawGraphics()

    def throwOnePlayer(self):
        dice = self.die[1][4]
        dice.throw()
        self.drawGraphics()
        for player in self.die:
            for score in player:
                print("Score:", score.face)


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
        pygame.display.update()

    def score(self):
        finalScore, summa = [], 0
        for player in self.die:
            for score in player:
                print(score.face)
                summa += int(score.face)
            finalScore.append(summa)
            summa = 0
        return finalScore


win = pygame.display.set_mode((500, 500))
active = Die()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

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
played = False
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
    for index, cords in enumerate(hitbox):
        x1, x2, y1, y2 = cords[0][0], cords[1][0], cords[0][1], cords[1][1]
        if x2 > mpos[0] > x1 and y2 > mpos[1] > y1:
            if hovering == 3:
                pygame.draw.rect(win, ([0, 255, 255]), [x1, y1, 100, 50], 0)
                text = myfont.render(messeges[index], False, (0, 0, 0))
                win.blit(text, (x1, y1))
                pygame.display.update()
                hovering = index
        elif hovering != 3 and hovering == index:
            cords = hitbox[hovering]
            x1, x2, y1, y2 = cords[0][0], cords[1][0], cords[0][1], cords[1][1]
            pygame.draw.rect(win, ([255, 255, 255]), [x1, y1, 100, 50], 0)
            text = myfont.render(messeges[index], False, (0, 0, 0))
            win.blit(text, (x1, y1))
            pygame.display.update()
            hovering = 3

    click = pygame.mouse.get_pressed()[0]
    if click:
        for index, cords in enumerate(hitbox):
            x1, x2, y1, y2 = cords[0][0], cords[1][0], cords[0][1], cords[1][1]
            if x2 > mpos[0] > x1 and y2 > mpos[1] > y1:
                # Spila
                if index == 0 and not played:
                    active.throwAllDie()
                    played = True
                # All
                elif index == 1:
                    active.win = True
                    active.throwAllPlayer()
                    running = False
                # One
                elif index == 2:
                    active.win = True
                    active.throwOnePlayer()
                    running = False

computer, player = active.score()
myfont = pygame.font.SysFont('Comic Sans MS', 60)
win.fill((0, 0, 0))

if computer > player:
    text = myfont.render('Þú tapaðir!', False, (255, 255, 255))
    win.blit(text, (80, 200))

elif computer < player:
    text = myfont.render('Þú vannst!', False, (255, 255, 255))
    win.blit(text, (80, 200))

elif computer == player:
    text = myfont.render('Jafntefli!', False, (255, 255, 255))
    win.blit(text, (80, 200))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False



