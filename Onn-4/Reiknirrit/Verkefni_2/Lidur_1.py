# Veit að ég átti ekki að gera keyranlegt forrit en langaði bara að prufukeyra sauðakóðann.

def binary_to_decimal(binary):
    if len(str(binary)) == 1:
        return int(binary)
    else:
        if binary[0] != "0":
            decimal_number = 2**(len(str(binary))-1)
        else:
            decimal_number = 0
        return decimal_number + binary_to_decimal(binary[1:])

print(binary_to_decimal("0100100001001"))