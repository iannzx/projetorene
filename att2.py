valor = float(input('Digite o valor da compra: R$'))
desc = float(input('Digite a porcentagem do desconto:'))

valor_desc =  valor * (desc / 100)
final = valor - desc
print('Valor final a pagar: R$', final)