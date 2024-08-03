import os
os.system("cls")

sonlar=[1.2, -2.4, 5.6, -8.1, -4.2, 3.1]

natija=list(map(lambda x: -x if x>0 else x*2, sonlar))
print(natija)