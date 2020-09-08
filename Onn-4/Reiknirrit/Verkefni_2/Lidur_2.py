def summa(n):
    if n == 0:
        print(n)
        return n
    else:
        fall = summa(n - 1)
        print(n)
        return n + fall
print(summa(5))
