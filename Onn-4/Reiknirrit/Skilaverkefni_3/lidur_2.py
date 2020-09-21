import random
import timeit

def randomList(size=10*10^6):
    listi = []
    for x in range(size):
        randomNr = random.randint(0, size)
        if randomNr not in listi:
            listi.append(randomNr)
    return listi

def isSorted(listi):
    for x, y in enumerate(listi[1:]):
        if(listi[x] > y):
            return False
    return True

def bubbleSort(listi=randomList()):
    comp = 0
    while True:
        if isSorted(listi):
            return listi

        for x in range(len(listi)-1):
            if(listi[x] > listi[x+1]):
                temp = listi[x]
                listi[x] = listi[x+1]
                listi[x+1] = temp
        comp += 1

def pythonSort(listi=randomList()):
    listi.sort()

print(timeit.timeit(bubbleSort))
print(timeit.timeit(pythonSort))

print(bubbleSort())