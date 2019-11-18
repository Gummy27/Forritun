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

def gr(listi):
    print('----------------------------')
    for tes in listi:
        print(tes)
    sleep(10)


# Class to maintain and store the grid the graphics are based on.
class Grid():
    def __init__(self):
        self.playing_field = []
        for x in range(19):
            temp = []
            for i in range(14):
                temp.append('_')
            self.playing_field.append(temp)

        self.blocks = []

    # Appends itmes to the self.blocks list.
    def append(self, object):
        self.place_on_grid(object)
        self.blocks.append(object)


    # Checks if any rows have been cleared. If so it executes the clear function
    def check_if_cleared(self):
        lines_cleared = []
        for index, line in enumerate(self.playing_field):
            clear = 0
            for value in line:
                if value != '_':
                    clear += 1

            if clear == len(line):
                lines_cleared.append(index)

        if len(lines_cleared) > 0:
            self.clear(lines_cleared)

    # Used to clear a row of blocks after a successfull alignment
    def clear(self, lines_cleared):
        for index in lines_cleared:
            del self.playing_field[index]
            self.playing_field = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]+self.playing_field
            grid.drawGraphics()

    # Places the blocks on the grid
    def place_on_grid(self, obj):
        for y, values in enumerate(obj.shape):
            for x, value in enumerate(values):
                if value != '*':
                    self.playing_field[obj.y+y][obj.x+x] = obj.index


    # Draws graphics based on self.playing_field
    def drawGraphics(self):
        win.fill((0,0,0))

        for y, values in enumerate(self.playing_field):
            for x, value in enumerate(values):
                if value != '_':
                    pygame.draw.rect(win, (litir[int(value)]), [x*size, y*size , size, size], 0)
        pygame.display.update()


    # Checks for any collisions. Returns False if collisions, True if not.
    def collision(self, x, y):
        obj = self.blocks[-1]
        if x > -1:
            pass
            try:
                for yy, listi in enumerate(obj.shape):
                    for xx, bool in enumerate(listi):
                        if bool == '#':
                            if self.playing_field[y+yy][x+xx] != '_':
                                return False
                return True
            except:
                return False
        else:
            return False


class Block():
    def __init__(self):
        self.x = 6
        self.y = 0
        self.playing = True

        self.index = randint(0, 6)
        self.shape = shapes[self.index]

    def move(self, x, y, down=False):
        if grid.collision(self.x + x, self.y + y):
            self.x += x
            self.y += y
        elif down:
            self.playing = False

    def rotate(self):
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

resolution = (350, 475)

start_time_down = time()
start_time_move = time()

pygame.init()
pygame.font.init()

size = 25
win = pygame.display.set_mode(resolution)
# game = Battlefield(resolution)

pygame.display.set_caption("First Game")

grid = Grid()
running = True
while running:
    grid.append(Block())

    grid.drawGraphics()

    while grid.blocks[-1].playing and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Checks if time passed is more than 2 seconds
        if time() - start_time_down > 2:
            # True means a possible down collision that results in spawning a new block
            if grid.blocks[-1].move(0, 1, True): # Checks if the next move collides.
                grid.place_on_grid(grid.blocks[-1])
                grid.drawGraphics()

                # Restarts the clock until the block is moved down once more.
                start_time_down = time()

        keys = pygame.key.get_pressed()
        moves = [
            [keys[pygame.K_LEFT], 'left'],
            [keys[pygame.K_RIGHT], 'right'],
            [keys[pygame.K_UP], 'up'],
            [keys[pygame.K_DOWN], 'down']
        ]
        # This for loops loops through all the moves that the game responds to.
        for move in moves:
            # Checks if the button has been pressed and that enough time has passed for another move
            if move[0] and time() - start_time_move > 0.1:
                print("ok")
                # Left button
                if move[1] == 'left':
                    grid.blocks[-1].move(-1, 0) # Moves the player -1 x

                # Right Button
                if move[1] == 'right':
                    grid.blocks[-1].move(1, 0) # Moves the player +1 x

                # Up button
                if move[1] == 'up':
                    grid.blocks[-1].rotate() # Rotates the player

                # Down button
                if move[1] == 'down':
                    grid.blocks[-1].move(0, 1, True) # Moves the player +1 y

                # Graphics are drawn after all if statements have been checked
                grid.drawGraphics()

                # time till another move can be initiated is reset.
                start_time_move = time()
    grid.check_if_cleared()

grid = Grid()