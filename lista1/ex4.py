#4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = int(input("salario: "))
aumento = int(input("porcentagem aumento: "))
valor_aumento = (salario * aumento) / 100
novo_salario = salario + valor_aumento
print("valor do aumento -> R$%d" %valor_aumento)
print("novo_salario -> R$%d" %novo_salario)
