def thversumma(n):
    if n == 0:
        return 0
    else:
        x = int(str(n)[0])
        pop = x*10**(len(str(n))-1)
        return x + thversumma(n-pop)

print(thversumma(1206))
    
