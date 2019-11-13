import pygame
from random import choice
from time import time, sleep
import csv

shapes = []
with open('shapes.csv', 'r') as file:
    listi = list(csv.reader(file, delimiter=' '))
    for shape in listi:
        shapes.append(list(csv.reader(shape)))

class Shape():
    def __init__(self):
        self.shape = choice(shapes)
        self.moving = True

        self.calculateWidthHeight()

    def rotate(self):
        size_of_matrix = len(self.shape)
        matrix = []
        for x in range(size_of_matrix):
            matrix.append([])
            for i in range(size_of_matrix):
                matrix[x].append('*')
        print(matrix)

        for x in range(size_of_matrix):
            for y in range(size_of_matrix):
                matrix[x][y] = self.shape[::-1][y][x]

        self.shape = matrix
        self.calculateWidthHeight()

    def calculateWidthHeight(self):
        loop = len(self.shape)
        self.height, self.width = 0, 0
        for x in range(loop):
            highest, widest = 0, 0
            for i in range(loop):
                if self.shape[i][x] == '#':
                    highest += 1
                if self.shape[x][i] == '#':
                    widest += 1
            if self.height < highest:
                self.height = highest

            if self.width < widest:
                self.width = widest

        self.height *= size


    def drawShape(self, x, y):
        win.fill((0, 0, 0))
        for yy, listi in enumerate(self.shape):
            for xx, bool in enumerate(listi):
                if bool == '#':
                    pygame.draw.rect(win, (255, 255, 255), [x + size * xx, y + size * yy, size, size], 0)
        pygame.display.update()

    def collision(self, x, y):
        if y + size + self.height < 500 - size:
            return True
        else:
            self.moving = False
            return False

# your code
start_time_down = time()
start_time_move = time()

pygame.init()
pygame.font.init()

size = 25
win = pygame.display.set_mode((500, 475))

pygame.display.set_caption("First Game")


running = True

while running:
    x, y = 100, 100

    player = Shape()
    player.drawShape(x, y)
    pygame.display.update()
    while player.moving:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False

        if time() - start_time_down > 1.5:
            if player.collision(x, y):
                y += size
                player.drawShape(x, y)

            start_time_down = time()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and time() - start_time_move > 0.2:
            x -= size

            player.drawShape(x, y)

            start_time_move = time()
            start_time_down = time()

        if keys[pygame.K_RIGHT] and time() - start_time_move > 0.2:
            x += size

            player.drawShape(x, y)

            start_time_move = time()
            start_time_down = time()

        if keys[pygame.K_UP] and time() - start_time_move > 0.2:
            player.rotate()
            player.drawShape(x, y)

            start_time_move = time()
            start_time_down = time()

        if keys[pygame.K_DOWN] and time() - start_time_move > 0.2:
            if player.collision(x, y):
                y += size
                player.drawShape(x, y)

            start_time_down = time()
            start_time_move = time()


