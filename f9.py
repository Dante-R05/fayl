import os
os.system("cls")

sonlar=[-10, 20, -50, 70, 150, -270]

natija=list(filter(lambda x: x>0, sonlar))
print(natija)