'''5.Faça um Programa que leia três números e mostre o maior e o menor deles.'''
a,b,c = input("Informe 3 valores separados por espaço: ").split(' ')
a = int(a)
b = int(b)
c = int(c)
maior, menor = 0,0

if a > b > c or a > c > b:
    maior = a
elif b > c > a or b > a > c:
    maior = b
else:
    maior = c

if a < b < c or a < c < b:
    menor = a
elif b < a < c or b < c < a:
    menor = b
else:
    menor = c

print("maior = %d"%maior)
print("menor = %d"%menor)