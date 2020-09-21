def summa(n):
    if n == 1:
        print(n, end="²=")
        return n**2
    else:
        print(n, end="²+")
        fall = summa(n - 1)
        return n**2 + fall
print(summa(5))
