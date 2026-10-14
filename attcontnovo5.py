vetor = []
par = []
impar = []

for i in range(20):
    numero = int(input('Digite o ' + str(i + 1) + 'º número: '))
    vetor.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print('Vetor:', vetor)
print('Pares:', par)
print('Ímpares:', impar)
