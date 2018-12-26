'''valor_fatorial = int(input("Insira a fatorial que deseja: "))
total_fatorial = 1
while valor_fatorial != 0:
    total_fatorial = total_fatorial * valor_fatorial
    valor_fatorial -= 1
print("O fatorial é: %d"%total_fatorial)'''

i = 1
fat = 1
n = int(input("Digite n: "))
while i <= n:
    fat *= i
    i += 1
print("fatorial de (%d) --> %d"%(n, fat))