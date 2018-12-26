'''Faça um programa que leia um vetor de 10 caracteres minúsculos, e diga
quantas consoantes foram lidas'''

caracteres = []
vogais = ['a','e','i','o','u']
i = 1
consoantes = 0
while i <= 10:
    n = input()
    caracteres.append(n)
    if n not in vogais:
        consoantes += 1
    i += 1
print("Total consoantes: %i" %consoantes)
