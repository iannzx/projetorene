salario = float(input("Digite o salário: R$ "))

if salario > 0 and salario <= 280:
    percentual = 20
else:
    if salario > 280 and salario <= 700:
        percentual = 15
    else:
        if salario > 700 and salario <= 1500:
            percentual = 10
        else:
            percentual = 5

aumento = salario * percentual / 100
novo_salario = salario + aumento

print("Salário antes do reajuste: R$", salario)
print("Percentual de aumento:", percentual, "%")
print("Valor do aumento: R$", aumento)
print("Novo salário: R$", novo_salario)