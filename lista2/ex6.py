'''6.Faça um Programa que pergunte quanto você ganha por hora e o número
 de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
 referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
 8%  para  o  INSS  e  5%  para  o  sindicato,  faça  um  programa  que  
 nos  dê  o  salário  bruto,  quanto  pagou  ao  INSS, quanto pagou ao sindicato
 e o salário líquido. Observe que Salário Bruto -Descontos = Salário Líquido.
 Calcule os descontos e o salário líquido, conforme a tabela abaixo:
    a.+ Salário Bruto : R$
    b.-IR (11%) : R$
    c.-INSS (8%) : R$
    d.-Sindicato ( 5%) : R$
    e.= Salário Liquido : R'''

grana = float(input("salário por hora: "))
horas_trabalhadas = int(input("horas trabaladas no mês: "))
salario_bruto = grana * horas_trabalhadas
ir = (salario_bruto * 11)/ 100  #desconto de 11%
inss = (salario_bruto * 8)/ 100 #desconto de 8%
sindicato = (salario_bruto * 5) / 100 # desconto de 5%
salario_liquido = salario_bruto - ir - inss - sindicato
print("Sálario Bruto: %.2f"%salario_bruto)
print("IR = %.2f"%ir)
print("INSS = %.2f"%inss)
print("Sindicato: %.2f"%sindicato)
print("salario_liquido: %.2f"%salario_liquido)