texto = "The Python Software Foundation and the global Python community \
welcome and encourage participation by everyone. Our community is based on \
mutual respect, tolerance, and encouragement, and we are working to help each \
other live up to these principles. We want our community to be more diverse: \
whoever you are, and whatever your background, we welcome you."

texto.split(' ')
resultado = []
k = 0
texto2 = ""
while k < len(texto):
    if texto[k] in ",.;/<>:?!@#$%&*()_+=-][{}´`~^ºª§\|°":
        texto2 += ""
    else:
        texto2 += texto[k]
    k += 1

palavras = texto2.split(' ')
prefixos = ["P","p","Y","y","T","t","H","h","O","o","N","n"]
for x in palavras:
    if x.startswith(tuple(prefixos)) and x.endswith(tuple(prefixos)):
        resultado.append(x)

print(resultado) 
