
numeros = []

for i in range(5):
    numero = int(input('Digite um número inteiro: '))
    numeros.append(numero)

soma = sum(numeros)

multiplicacao = 1
for numero in numeros:
    multiplicacao *= numero

print('Números:', numeros)
print('Soma:', soma)
print('Multiplicação:', multiplicacao)
