#Questão 7

i = 1
maior = 0

while i <= 5:
    numero = float(input("Digite um número: "))

    if numero > maior:
        maior = numero

    i += 1

print("Maior número:", maior)
