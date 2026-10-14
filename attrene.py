nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário mensal: "))
emprestimo = float(input("Digite o valor do empréstimo: "))
meses = int(input("Digite em quantos meses deseja pagar: "))

parcela = emprestimo / meses
limite = salario * 0.32

if idade >= 18 and parcela <= limite:
    print("Empréstimo APROVADO!")
    print("Cliente:", nome)
    print("Valor da parcela: R$", parcela)
else:
    print("Empréstimo NEGADO!")