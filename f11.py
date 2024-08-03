import os
os.system("cls")

sonlar=[1, 0, 1, 1, 0, 0, 1, 0, 1, 1]

natija=list(map(lambda x: True if x==1 else False, sonlar))
print(natija)