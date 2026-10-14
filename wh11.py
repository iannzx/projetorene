#Questão 11

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

soma = 0

while a <= b:
    print(a)
    soma += a
    a += 1

print("Soma:", soma)
