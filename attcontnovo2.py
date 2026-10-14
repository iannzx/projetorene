vetor = []

for i in range(10):
    numero = float(input(f'Digite o {i + 1}º número real: '))
    vetor.append(numero)

print("Números na ordem inversa:")
print(vetor[::-1])
