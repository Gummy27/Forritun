listi = [2, 3, 3, 5, 6, 7, 9, 10]
print(listi)
while True:
    tala = int(input())
    if listi[-1] < tala:
        listi.append(tala)
    else:
        for index, value in enumerate(listi): 
            if value > tala:
                listi.insert(index, tala)
                print("ok")
                break
    print(listi)
