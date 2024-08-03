import os
os.system("cls")

sonlar=[10, 20, 50, 70, 150, 270]
n=int(input("N ni kiriting: "))
kub=n**3
print(kub)
natija=list(filter(lambda x: x>kub, sonlar))
print(natija)