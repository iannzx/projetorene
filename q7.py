fatias = int(input('Digite a quantidade de fatias: '))
amg = int(input('Digite a quantidade de amigos: '))

total1= fatias // amg
sobra = fatias % amg

print('Cada amigo vai receber: ', total1, 'fatias')
print('Sobrarão: ', sobra, 'fatias')