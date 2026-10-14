boleto = float(input('Digite o valor: R$'))
multa = 15.00
juros = boleto * 0.02
total = boleto + multa + juros

print('Valor do boleto; R$', boleto)
print('Multa: R$', multa)
print('Juros: R$', juros)
print('Total a pagar: R$', total)