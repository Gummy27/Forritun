from randomList import *

def isSorted(listi):
    for x, y in enumerate(listi[1:]):
        if(listi[x] > y):
            return False
    return True

def bubbleSort(listi):
    comp = 0
    while True:
        if isSorted(listi):
            return listi, comp

        for x in range(len(listi)-1):
            if(listi[x] > listi[x+1]):
                temp = listi[x]
                listi[x] = listi[x+1]
                listi[x+1] = temp
        comp += 1
        
print(bubbleSort(randomList()))