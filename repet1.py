# construa  um algoritmo que o nome de 150 pessoas e verifique 
# quantas possuem  maria no nome, exiba o total no final.

qntd = 0

for i in range(7):
    nome = input('Digite o nome da pessoa: ')

    if 'maria' in nome:
        qntd = qntd + 1

print('Total de pessoas com Maria no nome:', qntd)
