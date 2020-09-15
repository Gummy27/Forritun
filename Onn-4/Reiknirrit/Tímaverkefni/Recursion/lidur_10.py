def runa(n):
    if len(n) == 1:
        print(n)
    else:
        print(n)
        runa(n[1:])

runa("Guðmundur")