def bubbleSort(listi):
    listi = listi[:]
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
    return listi