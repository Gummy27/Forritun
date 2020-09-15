def runa(n):
    if n == 1:
        print(1)
    else:
        runa(n-1)
        print(n)

runa(5)
        