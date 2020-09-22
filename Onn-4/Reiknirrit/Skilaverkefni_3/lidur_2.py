import random
import time
from myBubbleSort import bubbleSort
from netBubbleSort import bubbleSortWeb

def randomList(size):
    listi = []
    for x in range(size):
        listi.append(random.randint(0, size))
    return listi

def timing(func, listi):
    start = time.time()
    func(listi)
    timeString = str(time.time() - start)
    return timeString+" "*(22-len(timeString))

def pythonSort(listi):
    start = time.time()
    listi.sort()
    timeString = str(time.time() - start)
    return timeString+" "*(22-len(timeString))

sizeOfList = int(input("Hve stóran lista viltu að algrímin raða? : "))
randomizedList1 = randomList(sizeOfList)
randomizedList2 = randomList(sizeOfList)
backwardsList = list(range(sizeOfList, 0, -1))


print("Algrím:                              | Random Listi Tilraun 1 | Random Listi Tilraun 2 | Versta Tilvik ")
print("Bubble sort algrímið mitt:           |", 
      timing(bubbleSort, randomizedList1), 
      "|", timing(bubbleSort, randomizedList2),
      "|", timing(bubbleSort, backwardsList))

print("Bubble sort sem tekið var af netinu: |", 
       timing(bubbleSortWeb, randomizedList1), 
       "|", timing(bubbleSortWeb, randomizedList2), 
       "|",timing(bubbleSortWeb, backwardsList))

print("Innbyggða python röðunar algrímið:   |", 
       pythonSort(randomizedList1), 
       "|", pythonSort(randomizedList2) , 
       "|",pythonSort(backwardsList))
