a = []

for i in range(10):
    num = int(input('Digite um número: '))
    a.append(num)

soma = 0

for num in a:
    soma = num **2

print('A soma dos quadrados dos elementos é:', soma)