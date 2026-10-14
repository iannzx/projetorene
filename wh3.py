#Questão 3

nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salário: "))
sexo = input("Sexo (f/m): ")
estado = input("Estado civil (s/c/v/d): ")

while nome == "" or idade < 0 or idade > 150 or salario <= 0 or sexo != "f" and sexo != "m" or estado != "s" and estado != "c" and estado != "v" and estado != "d":
    print("Dados inválidos! Digite novamente.")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    salario = float(input("Salário: "))
    sexo = input("Sexo (f/m): ")
    estado = input("Estado civil (s/c/v/d): ")

print("Cadastro realizado!")
