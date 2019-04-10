'''arquivo = open('mumeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()'''

with open('mumeros.txt') as f:
    print(f.read())