vetor = []
consoantes = []

for i in range(10):
    caractere = input(f'Digite o {i + 1}º caractere: ')
    vetor.append(caractere)

    if caractere.isalpha() and caractere.lower() not in 'aeiou':
        consoantes.append(caractere)

print('Quantidade de consoantes:', len(consoantes))
print('Consoantes:', consoantes)
