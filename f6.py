import os
os.system("cls")

sonlar=[12, 2.4, 56, 8.1, 42, 3.1]

natija=list(filter(lambda x: isinstance(x, int), sonlar))
print(natija)