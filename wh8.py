#Questão 8

i = 1
soma = 0

while i <= 5:
    numero = float(input("Digite um número: "))
    soma += numero
    i += 1

media = soma / 5

print("Soma:", soma)
print("Média:", media)
