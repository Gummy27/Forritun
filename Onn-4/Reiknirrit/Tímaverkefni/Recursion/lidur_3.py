def runa(n):
    if n == 0:
        print(0)
        return 2
    
    else:
        fall = runa(n-1)
        if fall > n:
            return fall
        print(fall)
        return fall + 2

runa(19)
