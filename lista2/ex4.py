'''4. Faça um Programa que leia três números e mostre o maior deles. '''

a,b,c = input("informe 3 numeros separados por espaço: ").split(' ')
a = int(a)
b = int(b)
c = int(c)

if a > b > c or a > c > b:
    print(a)
elif b > a > c or b > c > a:
    print(b)
else:
    print(c)