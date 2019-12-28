from board_generator import *
from random import randint

board = board_generator(16)

# board = [[0, 1, 0],[0, 1, 1],[0, 0, 0]]

# cords = [randint(0, 15), randint(0, 15)]
cords = [0, 0]

values, reveal = [], []
around = [
        [0, 1],
        [1, 1],
        [1, 0],
        [0, -1],
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [1, -1]
    ]

def huge_reveal(board, cords):
    # print("Reveal :", reveal)
    for x, y in around:

        try:
            if cords[0]+x > -1 and cords[1]+y > -1 and [cords[0]+x, cords[1]+y] not in reveal:
                values.append([cords[0]+x, cords[1]+y])
                if board[cords[0]+x][cords[1]+y] == 0:
                    reveal.append([cords[0]+x, cords[1]+y])
                    values.append(huge_reveal(board, [cords[0]+x, cords[1]+y]))
        except:
            pass

    return values

blocks_to_be_revealed, blank_blocks = [], []
def test(board, cords):
    global blocks_to_be_revealed
    for i, z in around:
        x, y = cords[0]+i, cords[1]+z
        # If the if sentence tries to index a non existing index in an object it automatically stops
        try:
            board[x][y]
            # This if statement checks if the values are Natural numbers (Above zero)
            if x > -1 and y > -1:
                # This if statement checks if the block to be revealed is already in the list so that the program won't stack overflow
                if [x, y] not in blank_blocks:
                    blocks_to_be_revealed.sort()
                    # print([x, y], blocks_to_be_revealed)
                    print(i, z, ':', x, y)
                    if [x, y] not in blocks_to_be_revealed:
                        blocks_to_be_revealed += [[x, y]]
                    if board[x][y] == 0:
                        # Blank blocks gathers cords for blocks that are blank and is used in the if statement above to avoid stack overflow
                        blank_blocks.append([x, y])
                        test(board, [x, y])
                        # blocks_to_be_revealed += test(board, [x, y])

        except:
            pass

    blocks_to_be_revealed.sort()
    return blocks_to_be_revealed

# Prints Out the board
for index_x, x in enumerate(board):
    for index_y, i in enumerate(x):
        if cords == [index_x, index_y]:
            print("X", end=" | ")
        elif i < 9:
            print(i, end=" | ")
        else:
            print("B", end=" | ")
    print("\n"+"-"*8*4*2)

print(test(board, cords))

'''
print(len(test(board, cords)), end=": ")
for x, y in test(board, cords):
    print(x, y)
    print(board[x][y], end=" ")
'''