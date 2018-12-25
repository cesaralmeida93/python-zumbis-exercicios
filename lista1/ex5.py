#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
#preço a pagar.
preco = float(input("preço: "))
porcentagem_desconto = int(input("porcentagem de desconto: "))
valor_desconto = (preco * porcentagem_desconto) / 100
preco_pagar = preco - valor_desconto
print("o valor do desconto é R$%.2f" %valor_desconto)
print("o praço a pagar é R$%.2f" %preco_pagar)