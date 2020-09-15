def thversumma(n):
    if n == 1:
        return 1
    else:
        return n+thversumma(n-1)

print(thversumma(100))