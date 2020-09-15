from time import *
from keyboard import is_pressed


while True:
    if is_pressed("Space"):
        beginning = time()
        while not is_pressed("Space"):
            pass
        print(time() - beginning)

print("This is kinda cool!")