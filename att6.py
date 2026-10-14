preco = float(input('Digite o preço: R$'))

avista = preco - (preco * 0.05)
parce = preco + (preco * 0.08)

print('Valor à vista: R$', avista)
print('Valor no cartão: R$', parce)