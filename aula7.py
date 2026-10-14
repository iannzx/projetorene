saque = int(input('Digite um valor inteiro em R$: '))

nota100 = saque // 100
resto = saque % 100

nota50 = resto // 50
resto = resto % 50

nota20 = resto // 20
resto = resto % 20

nota10 = resto // 10
resto = resto % 10

nota2 = resto // 2
resto = resto % 2

nota1 = resto

print(nota100)
print(nota50)
print(nota20)
print(nota10)
print(nota2)
print(nota1)