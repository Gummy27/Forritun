import pygame
from random import randint
from time import sleep

grid = 64
size = 15

resolution = (size*grid, size*grid)

pygame.init()
pygame.font.init()

win = pygame.display.set_mode(resolution)

pygame.display.set_caption('MineSweeper')

for x in range(grid//2):
    for i in range(grid//2):
        pygame.draw.rect(win, (192, 192, 192), [x*size*2, i*size*2, size*2, size*2], 0)
        pygame.draw.rect(win, (0, 0, 0), [x*size*2, i*size*2, size*2, size*2], 1)
pygame.display.update()

running = True

def changeBlock(x, y):
    print("Hann kom hér í gegn")
    print(x*size*2, y*size*2)
    pygame.draw.rect(win, (255, 0, 0), [(x-1)*size*2, (y-1)*size*2, size*2, size*2], 0)
    pygame.draw.rect(win, (0, 0, 0),   [(x-1)*size*2, (y-1)*size*2, size*2, size*2], 1)
    pygame.display.update()

while running:
    print("Ok")
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        # print(x, y)

        index = [0, 0]
        for i in range(grid):
            if x <= i*size*2 and index[0] == 0:
                index[0] = i

            if y <= i*size*2 and index[1] == 0:
                index[1] = i

            if index[0] != 0 and index[1] != 0:
                break
        print(index)
        changeBlock(index[0], index[1])



