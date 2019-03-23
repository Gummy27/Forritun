teljari = int(input())
listi = []
for x in range(teljari):
    for_teljari = 0
    for_teljari_2 = 0
    nei = 0
    nafn=input()
    upprunalega = ""
    stadur=input()
    for i in listi:
        for y in i:
            if(y != " "):
                upprunalega = str(upprunalega) + str(y)
                for_teljari_2 += 1
            else:
                break
        if(stadur == upprunalega):
            tala = int(i[for_teljari_2:]) + 1
            listi[for_teljari] = stadur + " " + str(tala)
            nei = 1
        for_teljari += 1
    if(nei == 0):
        listi.append(str(stadur)+" 1")

for x in listi:
    print(x)


