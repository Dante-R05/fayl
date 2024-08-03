import os
os.system("cls")

sonlar=[12, 2.4, 56, 8.1, 42, 3.1]

natija=list(map(lambda x: float(x) if isinstance(x, int) else int(x), sonlar))
print(natija)