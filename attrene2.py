#construa uma calculadora  lendo os numeros e as operações. mostre na tela os resultados.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Não é possível dividir por zero!"
else:
    resultado = "Operação inválida!"

print("Resultado:", resultado)