'''n = 1
soma = 0
while n <= 10:
    x =  int(input("Digite o %dº número: " %n))
    soma = soma + x
    n = n + 1
print("Soma: %d" %soma)'''

n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o %dº número: "%n))
    soma += x
    n += 1
print("Média: %5.2f" %(soma/10))
