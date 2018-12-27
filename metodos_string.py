'''Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e imprima com o nome do mês por extenso'''
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
dia, mes, ano = input('data (dd/mm/aaaa)').split('/')
print('Você nasceu em: ')
print('%s de %s de %s' %(dia, meses[int(mes) -1], ano))