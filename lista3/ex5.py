"""5.Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides. """
dividendo = int(input("Valor 1: "))
divisor = int(input("Valor 2: "))
while divisor != 0:
    temp = divisor
    divisor = dividendo % divisor
    dividendo = temp
print(dividendo)