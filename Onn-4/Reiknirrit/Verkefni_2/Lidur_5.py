def samnefnari(n, m):
    if(m==0):
        return n
    else:
        return samnefnari(m, n%m)

print(samnefnari(13, 3))