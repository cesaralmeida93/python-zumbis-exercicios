"""2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações."""

nome = input("Nome do usuário: ")
senha = input("Senha: ")
while nome == senha:
    print("Nome do usuário não pode ser igual a senha!")
    nome = input("Nome do usuário: ")
    senha = input("Senha: ")
print("Nome: %s"%nome)
print("Senha: %s"%senha)