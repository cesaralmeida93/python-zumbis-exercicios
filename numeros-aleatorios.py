'''import random
lista = []
for i in range(15):
    lista.append(random.randint(10, 100))
print(lista)'''

import random
lista = []
while len(lista) < 15:
    x = random.randint(10, 100)
    if x not in lista:
        lista.append(x)
lista.sort()
print(lista)