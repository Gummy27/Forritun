import pygame
from random import choice
from time import time, sleep
import csv

shapes = []
with open('shapes.csv', 'r') as file:
    listi = list(csv.reader(file, delimiter='-'))
    for shape in listi:
        shapes.append(list(csv.reader(shape)))

class Shape():
    def __init__(self):
        self.shape = choice(shapes)

    def drawShape(self, x, y):
        win.fill((0, 0, 0))
        for yy, listi in enumerate(self.shape):
            print(listi)
            for xx, bool in enumerate(listi):
                if bool == '1':
                    pygame.draw.rect(win, (255, 255, 255), [x + size * xx, y + size * yy, size, size], 0)
        pygame.display.update()


# your code
start_time_down = time()
start_time_move = time()

pygame.init()
pygame.font.init()

size = 25
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")


running = True
x, y = 100, 100
pressed = False

player = Shape()

player.drawShape(x, y)

pygame.display.update()
while running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False

    if time() - start_time_down > 0.8:
        player.drawShape(x, y)

        start_time_down = time()
        y += size

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

