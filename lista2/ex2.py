'''2. Determine se um ano é bissexto. Verifique no Google como fazer isso...'''
ano = int(input("Digite o ano: "))
if ano % 4 == 0 and ano % 100 != 0:
    print("Ano bissexto")
else:
    print("não é ano bissexto")