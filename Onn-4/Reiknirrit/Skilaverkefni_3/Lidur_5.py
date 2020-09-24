tala = int(input())

listi = [2, 3, 3, 5, 6, 7, 9, 10]

for index, value in enumerate(listi): 
    if value > tala:
        listi.insert(index, tala)
        break

print(listi)

# Þar sem forritið keyrir aðeins einu sinni í gegnum listann þá getur flækjustigið ekki verið verra en O(n).