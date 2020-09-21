def runa(n):
    if(n == 1):
        print(n, end=" ")
        return n
    else:
        x = runa(n-1)
        print(n+x, end=" ")
        return n+x

runa(5)