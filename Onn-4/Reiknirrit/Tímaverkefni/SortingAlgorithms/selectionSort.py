from randomList import *

def isSorted(listi):
    for x, y in enumerate(listi[1:]):
        if(listi[x] > y):
            return False
    return True

def selectionSort(listi):
    comp = 0

    while(True):
        biggest = comp
        for i, x in enumerate(listi[comp:]):
            if x <= listi[biggest]:
                biggest = i+comp

        # Víxlun á sér stað.
        temp = listi[comp]
        listi[comp] = listi[biggest]
        listi[biggest] = temp

        if isSorted(listi):
            return listi, comp

        comp += 1

    return listi

print(selectionSort(randomList()))