n1 = float(input('Digite sua a 1 nota: '))
n2 = float(input('Digite sua a 2 nota: '))
n3 = float(input('Digite sua a 3 nota: '))

media = ( n1 + n2 + n3) / 3

if media < 7:
    print('Você fará a nota final')

    prova = float(input('Digite a nota da prova final: '))

    if prova >= 5:
        print('Aprovado!')
    else:
        print('Reprovado!')

else:
    print('Aprovado!')