import random

def randomList(size=100):
    listi = []
    for x in range(size):
        randomNr = random.randint(0, 100)
        if randomNr not in listi:
            listi.append(randomNr)
    return listi
