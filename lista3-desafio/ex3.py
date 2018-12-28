'''Verifique se um inteiro positivo n é primo.'''
inteiro = int(input("número: "))
k = 1
divisores = 0
while k <= inteiro:
    if inteiro % k == 0:
        divisores = divisores + 1
    k += 1
print(divisores == 2)