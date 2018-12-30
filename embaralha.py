def embaralha(x):
    import random  
    lista = list(x)
    random.shuffle(lista)
    return ''.join(lista)

print(embaralha('santos tri-campeão'))