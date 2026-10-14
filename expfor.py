nome_maior = ''
nome_menor = ''
maior = 0
menor = 999
soma = 0
for pessoa in range(43):
    nome = input('Qual seu nome: ')
    alt = float(input('Qual sua altura? '))
    if alt > maior:
        maior = alt
    if alt < menor :
        nome_menor = nome
        menor = alt
        soma = soma + alt