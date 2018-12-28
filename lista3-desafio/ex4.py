'''Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando também a multiplicidade de cada fator.'''
numero = int(input("número: "))
for k in range(2, numero):
    while numero % k == 0:
        print(k)
        numero = numero / k