idades = []
alturas = []

for i in range(5):
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))

    idades.append(idade)
    alturas.append(altura)

for i in range(4, -1, -1):
    print('Idade:', idades[i], 'Altura:', alturas[i])
