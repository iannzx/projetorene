#Questão 12

numero = int(input("Digite um número de 1 a 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Número inválido. Digite de 1 a 10: "))

i = 1

print("Tabuada de", numero, ":")

while i <= 10:
    print(numero, "X", i, "=", numero * i)
    i += 1
