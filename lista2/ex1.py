'''1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.'''

ladoa,ladob,ladoc = input("Informe os 3 lados separados por espaço: ").split(' ')
ladoa = int(ladoa)
ladob = int(ladob)
ladoc = int(ladoc)

if abs(ladob - ladoc) < ladoa < (ladob + ladoc) and abs(ladoa - ladoc) < ladob < ladoa + ladoc and abs(ladoa - ladob) < ladoc < (ladoa + ladob):
    print("pode ser triangulo")
    if ladoa == ladob == ladoc:
        print("triangulo equilátero")
    elif (ladoa == ladob and ladob != ladoc) or (ladoa != ladob and ladob == ladoc) or (ladoa == ladoc and ladob != ladoc):
        print("triangulo isósceles")
    else:
        print(("triângulo obrtusângulo"))
else:
    print("não pode ser triangulo")