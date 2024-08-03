import os
os.system("cls")

malumotlar = [1, 'salom', 3.14, 'dunyo', 42, 'Python', True]

natija = list(filter(lambda x: isinstance(x, str), malumotlar))

print(natija)
