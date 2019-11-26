import pygame
from pygame.locals import *
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

def gr():
    print("-----------------")

class Grid():
    def __init__(self):
        self.scoreCount = 0
        self.playing_field = []
        for x in range(19):
            temp = []
            for i in range(14):
                temp.append('_')
            self.playing_field.append(temp)

        self.blocks = []

    def new_block(self):
        self.player = Block()
        self.place_player_on_grid(self.player)

    def save_player_to_grid(self):
        for row_index, row in enumerate(self.playing_field):
            for col_index, value in enumerate(row):
                if value[0] == 'p':
                    self.playing_field[self.player.y+row_index][self.player.x+col_index] = value[1]

    def place_player_on_grid(self, obj):
        for row_index, row in enumerate(self.playing_field):
            for col_index, value in enumerate(row):
                if value[0] == 'p':
                    self.playing_field[row_index][col_index] = '_'

        for y, values in enumerate(obj.shape):
            for x, value in enumerate(values):
                if value != '*':
                    self.playing_field[y][x] = 'p'+str(obj.index)

    def collision(self, x=0, y=0):
        x += self.player.x
        y += self.player.y
        try:
            for row, shape in enumerate(self.player.shape):
                for col, value in enumerate(shape):
                    # print(value, row+y, col+x, end=" | ")
                    # print(y+row, x+col)
                    # Check if the value is not a placeholder
                    if value != '*':
                        # Check if the value is not a placeholder
                        if x + col < 0:
                            return False
                        elif self.playing_field[y+row][x+col] != '_':
                            # Checking the value is not a part of a player indicator
                            if self.playing_field[y+row][x+col][0] != 'p':
                                return False
                # print()

            self.player.x = x
            self.player.y = y

            self.place_player_on_grid(self.player)
            return True
        except:
            return False

    def draw_graphics(self):
        win.fill((0,0,0))

        for row, values in enumerate(self.playing_field):
            for col, value in enumerate(values):
                if value[0] == 'p':
                    pygame.draw.rect(win, (litir[int(value[1])]), [(col+self.player.x) * size, (row+self.player.y) * size, size, size], 0)
                elif value != '_':
                    pygame.draw.rect(win, (litir[int(value)]), [col * size, row * size, size, size], 0)

        self.setUpScoreText()

        win.blit(self.score, self.scoreCords)
        pygame.display.update()

    def setUpScoreText(self):
        textColor = (255, 0, 0)
        bkgrColor = (0, 0, 0)
        font = pygame.font.Font('freesansbold.ttf', 32)

        self.score = font.render(f"Score: {self.scoreCount}", True, textColor, bkgrColor)
        self.scoreCords = self.score.get_rect()
        self.scoreCords.center = (350 // 2, 15)

    def check_if_clear(self):
        cleared_rows = []
        for row, values in enumerate(self.playing_field):
            clear = True
            for value in values:
                if value == '_':
                    clear = False
            if clear:
                cleared_rows.append(row)

        if len(cleared_rows) > 0:
            self.scoreCount += 100 * len(cleared_rows)

            for line in cleared_rows[::-1]:
                del self.playing_field[line]
            for x in range(len(cleared_rows)):
                self.playing_field = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_','_']] + self.playing_field

        grid.draw_graphics()


class Block():
    def __init__(self):
        self.x = 6
        self.y = 3
        self.playing = True

        self.index = randint(0, 6)
        self.shape = shapes[self.index]

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

pygame.display.set_caption("Tetris")

grid = Grid()

running = True
playing = True
while running:
    while playing:
        grid.new_block()
        if not grid.collision():
            playing = False

        while grid.player.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    grid.player.playing = False
                    running = False

            # Checks if time passed is more than 2 seconds
            if time() - start_time_down > 2:
                    if not grid.collision(y=1):
                        grid.player.playing = False

                    start_time_down = time()
                    grid.draw_graphics()

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
                    # Left button
                    if move[1] == 'left':
                        grid.collision(x=-1)

                    # Right Button
                    if move[1] == 'right':
                        grid.collision(x=1)

                    # Up button
                    if move[1] == 'up':
                        grid.player.rotate()
                        grid.place_player_on_grid(grid.player)

                    # Down button
                    if move[1] == 'down':
                        if not grid.collision(y=1):
                            grid.player.playing = False


                    start_time_move = time()
                grid.draw_graphics()

        grid.save_player_to_grid()
        grid.check_if_clear()

    textColor = (255, 0, 0)
    bkgrColor = (0, 0, 0)

    font = pygame.font.Font('freesansbold.ttf', 32)
    gameOver = font.render('Game Over!', True, textColor, bkgrColor)
    gameOverCords = gameOver.get_rect()
    gameOverCords.center = (350 // 2, 475 // 2)

    font = pygame.font.Font('freesansbold.ttf', 18)
    instructions = font.render('Press any key to play again', True, textColor, bkgrColor)
    instructionsCords = instructions.get_rect()
    instructionsCords.center = (350 // 2, 475 // 2+34)

    win.blit(gameOver, gameOverCords)
    win.blit(instructions, instructionsCords)
    pygame.display.update()

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
            break

        elif event.type == KEYDOWN:
            playing = True
            grid = Grid()
            break

