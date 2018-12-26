'''Faça um programa que leia quatro notas, mostre as notas e a média na tela'''
notas = []
i = 1
while i <= 4:
    n = float(input())
    notas.append(n)
    i += 1

soma = 0
i = 0
while i <= 3:
    soma += notas[i]
    i += 1

print("Notas: ", notas)
print("Média: %4.2f" %(soma/4))

'''
notas = []
soma = 0
i = 1
while i <= 4:
    n = float(input("Nota: "))
    notas.append(n)
    soma += n
    i += 1
print("Notas: ", notas)
print("Média: %4.2f" %(soma/4))
'''