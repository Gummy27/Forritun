from random import randint

def board_generator(size):
    board = []
    for x in range(size):
        temp = []
        for i in range(size):
            temp.append(0)
        board.append(temp)

    for x in range(16):
        x, y = randint(0, size-1), randint(0, size-1)
        board[x][y] = 9

        # Left side
        if x - 1 > -1:
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

for x in board_generator(8):
    for value in x:
        if value > 8:
            print('&', end=" | ")
        else:
            print(value, end=" | ")
    print("\n"+"-"*4*8)