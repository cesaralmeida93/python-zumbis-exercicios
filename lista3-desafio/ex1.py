'''Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
verificar se n é triangular.'''

numero = int(input("Informe o número: "))
k = 0
while k * (k + 1) * (k + 2) < numero:
    k = k + 1
print(k * (k + 1) * (k + 2) == numero)