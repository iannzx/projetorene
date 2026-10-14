#questão 2

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

while senha == usuario:
    print("Erro: a senha não pode ser igual ao nome de usuário!")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

print("Usuário e senha cadastrados com sucesso!")
