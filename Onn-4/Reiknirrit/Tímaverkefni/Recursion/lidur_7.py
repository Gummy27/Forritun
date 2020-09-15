def recursion(strengur):
    if len(strengur) == 1:
        try: 
            int(strengur[0])
            return 1
        except:
            return 0
    else:
        fall = recursion(strengur[1:])
        try: 
            int(strengur[0])
            return fall + 1
        except:
            return fall

print(recursion("123s5"))