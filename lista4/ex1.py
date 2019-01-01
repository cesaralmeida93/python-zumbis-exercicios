import random
lista = []
for i in range(10):
    lista.append(random.randint(10, 100))
lista.sort()
print(lista)
print('maior: %d' %lista[-1])
print('menor: %d' %lista[0])