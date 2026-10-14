# continue
# continue quando acionado dentro do laço, remete diretamente
# para o inicio da repetição

qntd = 0
nome = ''
while nome != 'fim':
    nome = input('Digite seu nome ou digite fim para encerrar: ')
    if nome =='rafael':
        continue
    elif nome == 'fim':
        break
    qntd = qntd + 1

    print('A quantidade final foi', qntd)