medias = []
aprovados = 0

for i in range(10):
    soma = 0

    for j in range(4):
        nota = float(input('Digite a nota: '))
        soma += nota

    media = soma / 4
    medias.append(media)

    if media >= 7:
        aprovados += 1

print('Número de alunos com média maior ou igual a 7.0:', aprovados)
