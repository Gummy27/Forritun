import math

#fall = input("Sláðu inn fallið: f(x)=")
#efriX = input("Sláðu inn x fyrir efri mörk:")
#nedriX = input("Sláðu inn x fyrir neðri mörk:")

fall = "x3+4x2-x1"

part = ""
diffra = []
for x in fall:
    if x == '+' or x == '-':
        diffra.append(part)
        if x == '-':
            part = x
        else:
            part = ""
    else:
        part += x

for x in diffra:

diffra.append(part)
print(diffra)