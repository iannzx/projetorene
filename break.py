#break
# é um comando usado para encerrar o laço de repetição
# Funciona em qualquer estrutura de repetição

resposta = 'nao'

while resposta != 'sim':
    resposta = input('Você aceita namorar cmg? ')
    if resposta == 'é o jeito':
        print('Eu nao quero mais')
    break

