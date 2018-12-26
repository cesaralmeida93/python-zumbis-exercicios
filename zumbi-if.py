'''a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
if a > b:
    print("O primeiro é maior!")
else:
    print("O segundo é maior!")

idade = int(input("Digite a idade de seu carro: "))
if idade <=3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")

velocidade = float(input("velocidade do carro: "))
if velocidade > 110:
    print("Multado!")
    multa = (velocidade - 110) * 5
    print("valor da multa: R$%.2f" %multa)

tempo_telefone = int(input("tempo falado: "))
if tempo_telefone < 200:
    cobranca = tempo_telefone * 0.20
elif tempo_telefone >= 200 or tempo_telefone <= 400:
    cobranca = tempo_telefone * 0.18
elif tempo_telefone > 400 and tempo_telefone <= 800:
    cobranca = tempo_telefone * 0.15
else:
    cobranca = tempo_telefone * 0.08

print("Conta telefonica: R$%6.2f" %cobranca)'''

x = 1
while x <= 3:
    print(x)
    x += 1