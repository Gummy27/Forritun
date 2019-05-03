'''
# lengd = int((8 - len(h2)) / 2 * 7)
# Prentuðu spilin eru 7 chr
# Fyrst er að finna hve mikið af spilum á að prenta út.
# Síðan er það sinnumað með 7 til að fá sama magn chr sem er á þessum spilum
# Síðan er það deilt með 2.
lengd = lambda l, t : int((l-8*t)*7/2)

input(len(5, 1))
fjoldi = 10
print("="*56)
print(" "*lengd(fjoldi, 1), end="")
for x in range(fjoldi):
    print("|     |", end="")
    if (x+1) % 8 == 0:
        print()
        print("="*lengd(fjoldi, 2), end="")
'''

strengur = ["1", "2", "3", "4", "5"]
strengur[1:].pop()
print(strengur)
