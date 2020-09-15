listi = ['a', 'e', 'i', 'o', 'u']

def recursion(n):
    if len(n) == 1:
        if n[0] in listi:
            return 1
        else:
            return 0
    else:
        fall = recursion(n[1:])
        if n[0] in listi:
            return fall + 1
        else:
            return fall

print(recursion("aeios"))
        