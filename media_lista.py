notas = [8, 5, 7, 3, 4.8]
i = 0
soma = 0
while i <= 4:
    soma += notas[i]
    i += 1
media = soma / 5
print("media: %.2f"%media)