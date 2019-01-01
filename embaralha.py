def embaralha(x):
    import random  
    lista = list(x)
    random.shuffle(lista)
    return ''.join(lista)

x = input('')
print(embaralha(x))