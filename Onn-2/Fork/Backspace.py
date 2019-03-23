nei = 1
word = input()
listi = []
listi_2 = []
for x in word:
    listi.append(x)
while(nei != 0):
    for_teljari = 0
    nei = 0
    for x in listi:
        if(x == ">"):
            print("ok")
            nei = 1
    for x in listi:
        if(x == ">"):
            print("Allt í lagi")
            listi[for_teljari] = ""
            listi[for_teljari-1] = ""
            break
        for_teljari += 1

for x in listi:
    print(x, end="")
 
