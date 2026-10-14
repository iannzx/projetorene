qntd = 0
nome = ''

while nome != 'fim':
    nome = input('Digite seu nome ou digite fim para encerrar: ')

    if nome == 'rafael':
        break

    if nome == 'fim':
        continue

    qntd = qntd + 1

print('A quantidade final foi', qntd)
