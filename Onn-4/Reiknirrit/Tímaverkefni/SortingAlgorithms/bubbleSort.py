from randomList import *
import time

def isSorted(listi):
    for x, y in enumerate(listi[1:]):
        if(listi[x] > y):
            return False
    return True

def bubbleSort1(listi=randomList()):
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

def bubbleSort2(listi):
    while True:
        comp = 0
        for x in range(len(listi)-1):
            if(listi[x] > listi[x+1]):
                temp = listi[x]
                listi[x] = listi[x+1]
                listi[x+1] = temp

                comp += 1
        if comp == 0:
            break


randomizedList = randomList(10**4)
start = time.time()
bubbleSort1(randomizedList)
print(time.time() - start)

start = time.time()
bubbleSort2(randomizedList)
print(time.time() - start)
