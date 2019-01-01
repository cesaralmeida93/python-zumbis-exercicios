import random
lista = []
par = []
impar = []
for i in range(20):
    lista.append(random.randint(1, 100))
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
lista.sort()
par.sort()
impar.sort()

print('lista: %s' %lista)
print('par: %s' %par)
print('impar: %s' %impar)


