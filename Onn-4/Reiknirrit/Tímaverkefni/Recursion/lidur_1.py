def runa(n):
    if n == 1:
        print(1)
        return 1
    else:
        fall = runa(n-1)*2
        print(fall)
        return fall

runa(5)