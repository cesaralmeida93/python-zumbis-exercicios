import random
lista1 = []
lista2 = []
lista3 = []
for i in range(10):
    lista1.append(random.randint(1, 100))
    lista2.append(random.randint(1, 100))
    lista3.append(lista1[i])
    lista3.append(lista2[i])

lista1.sort()
lista2.sort()
lista3.sort()
print(lista1)
print(lista2)
print(lista3)