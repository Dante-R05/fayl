import os
os.system("cls")

def tub(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

sonlar = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]

tub_sonlar = list(filter(tub, sonlar))

print(tub_sonlar)
