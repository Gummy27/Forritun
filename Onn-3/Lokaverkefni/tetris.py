import pygame
from random import randint
from time import time, sleep
import csv

shapes = []
litir = []
with open('shapes.csv', 'r') as file:
    listi = list(csv.reader(file, delimiter=' '))
    for shape in listi:
        # print(list(csv.reader(shape))[0:-1])
        shapes.append(list(csv.reader(shape))[0:-1])
        litur = list(map(int, list(shape[-1].split(','))))
        litir.append(tuple(map(int, litur)))

class Shape():
    def __init__(self, x, y):
        self.x, self.y = x, y
        index = randint(0, 6)
        self.shape = shapes[index]
        self.color = litir[index]
        self.moving = True

        self.calculateWidthHeight()

    def rotate(self):
        global x, y
        restoreShape = self.shape
        restoreHeight = self.height
        restoreWidth = self.width
        restoreHeightPos = self.heightPos
        restoreWidthPos = self.widthPos
        restoreX = x
        restoreY = y

        size_of_matrix = len(self.shape)
        matrix = []
        for a in range(size_of_matrix):
            matrix.append([])
            for i in range(size_of_matrix):
                matrix[a].append('*')

        for a in range(size_of_matrix):
            for b in range(size_of_matrix):
                matrix[a][b] = self.shape[::-1][b][a]

        self.shape = matrix
        self.calculateWidthHeight()

        if not self.leftCollision() or not self.rightCollision():
            self.shape = restoreShape
            self.height = restoreHeight
            self.width = restoreWidth
            self.heightPos = restoreHeightPos
            self.widthPos = restoreWidthPos
            x = restoreX
            y = restoreY

    def calculateWidthHeight(self):
        loop = len(self.shape)

        self.height = 0
        self.width = 0
        self.widthPos = 0
        self.heightPos = 0
        for x in range(loop):
            for i in range(loop):
                if self.shape[x][i] == '#':
                    self.height += size
                    break
            if self.height == 0:
                self.heightPos += size

        for x in range(loop):
            for i in range(loop):
                if self.shape[i][x] == '#':
                    self.width += size
                    break
            if self.width == 0:
                self.widthPos += size


        # print(f"Width: {self.width}    Height: {self.height}")

    def moved(self, x, y):
        self.x, self.y = x, y

    def drawShape(self):
        # game.drawBackground()
        # self.savePos = []
        for yy, listi in enumerate(self.shape):
            for xx, bool in enumerate(listi):
                if bool == '#':
                    pygame.draw.rect(win, self.color, [self.x + size * xx, self.y + size * yy, size, size], 0)
                    # self.savePos.append([int((self.x + size * xx)/size), int((self.y + size * yy)/size)])

    def downCollision(self):
        if y + self.height - self.heightPos < 475:
            return True
        else:
            # game.saveShapePos(self.savePos)
            self.moving = False
            return False

    def leftCollision(self):
        if x + self.widthPos > 0:
            return True
        else:
            return False

    def rightCollision(self):
        if x + self.width + self.widthPos < 350:
            return True
        else:
            return False

class Blocks():
    def __init__(self):
        self.blocks = []

        self.matrix = []
        for x in range(19):
            temp = []
            for i in range(14):
                temp.append('*')
            self.matrix.append(temp)

    def append(self, object):
        print(object.shape)
        for x in object.shape:
            pass


        self.blocks.append(object)

    def drawShapes(self):
        win.fill((0, 0, 0))

        for block in self.blocks:
            block.drawShape()

        pygame.display.update()

    # def collisions(self):
        # player = self.blocks[-1]
        # for block in self.blocks[0:-1]:
        #    for

    def placed(self):
        for yy, listi in enumerate(self.blocks[-1].shape):
            for xx, bool in enumerate(listi):
                if bool == '#':
                    self.matrix[int((self.blocks[-1].y + size * yy)/25)][int((self.blocks[-1].x + size * xx)/25)] = '#'
        for x in self.matrix:
            print(x)


resolution = (350, 475)

start_time_down = time()
start_time_move = time()

pygame.init()
pygame.font.init()

size = 25
win = pygame.display.set_mode(resolution)
# game = Battlefield(resolution)

pygame.display.set_caption("First Game")

blocks = Blocks()

running = True
while running:
    x, y = 150, 100

    blocks.append(Shape(x, y))
    blocks.drawShapes()

    pygame.display.update()

    while blocks.blocks[-1].moving and running:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False

        if time() - start_time_down > 1.5:
            if blocks.blocks[-1].downCollision():
                y += size
                blocks.blocks[-1].moved(x, y)
                blocks.drawShapes()

            start_time_down = time()

        keys = pygame.key.get_pressed()
        moves = [
            [keys[pygame.K_LEFT],'left'],
            [keys[pygame.K_RIGHT],'right'],
            [keys[pygame.K_UP],'up'],
            [keys[pygame.K_DOWN],'down']
        ]
        for move in moves:
            if move[0] and time() - start_time_move > 0.2:
                if move[1] == 'left' and blocks.blocks[-1].leftCollision():
                    x -= size

                elif move[1] == 'right' and blocks.blocks[-1].rightCollision():
                    x += size

                elif move[1] == 'up':
                    blocks.blocks[-1].rotate()

                elif move[1] == 'down' and blocks.blocks[-1].downCollision():
                    y += size

                blocks.blocks[-1].moved(x, y)
                blocks.drawShapes()

                start_time_move = time()
    blocks.placed()