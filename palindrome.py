'''Verifique se a palavra é palindrome'''
palavra = input("digite a palavra: ")
if palavra == palavra[::-1]:
    print("a palavra %s é palíndrome" %palavra)
else:
    print("a palavra %s não é palíndrome" %palavra)