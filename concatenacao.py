'''Faça um programa que leia uma palavra e troque vogais por "*" '''
palavra = input("palavra: ")
k = 0
troca = ""
while k < len(palavra):
    if palavra[k] in 'aeiou':
        troca = troca + "*"
    else:
        troca = troca + palavra[k]
    k += 1
print("Nova palavra: %s" %troca)