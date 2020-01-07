from random import randint

def board_generator(size):
    board = []
    for x in range(size):
        temp = []
        for i in range(size):
            temp.append(0)
        board.append(temp)

    for i in range(size*size//9):
        x, y = randint(0, size-1), randint(0, size-1)
        board[x][y] = 9

        # Left side
        if x-1 > -1:
            rn = board[x-1]

            # Above
            if y + 1 < size:
                rn[y+1] += 1

            # Middle
            rn[y] += 1

            # Bottom
            if y - 1 > -1:
                rn[y-1] += 1

        if x + 1 < size:
            rn = board[x+1]

            # Above
            if y + 1 < size:
                rn[y+1] += 1

            # Middle
            rn[y] += 1

            # Bottom
            if y - 1 > -1:
                rn[y-1] += 1

        # Straight Above
        if y + 1 < size:
            board[x][y+1] += 1

        # Straight Down
        if y - 1 > -1:
            board[x][y-1] += 1

    return board

blocks_to_be_revealed, blank_blocks = [], []
def huge_reveal(board, cords):
    global blocks_to_be_revealed
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
                        huge_reveal(board, [x, y])

        except:
            pass

    blocks_to_be_revealed.sort()
    return blank_blocks, blocks_to_be_revealed
