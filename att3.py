salario = float(input('Digite o salário: R$'))
aumento = float(input('Digite a porcentagem de aumento: R$'))

va = salario * (aumento / 100)
novo = salario + va
print('Valor do aumento: R$', va)
print('Novo salário: R$', novo)