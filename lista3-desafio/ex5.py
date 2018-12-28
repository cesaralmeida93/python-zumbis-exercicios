'''Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321'''
n = int(input("Número: "))
inv = 0
while n > 0:
    inv = inv * 10
    inv = inv + (n % 10)
    n = n // 10
print(inv)

'''
n = input('número: ')
n = n[::-1]
print(n)
'''