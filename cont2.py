# o professor flavio de calculo 1, pediu para voce construir um algoritmo em python para receber do usuario os 3 lados de um triagulo, o programa deve informar se o triangulo é equilatero ou nao.

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Verificando-se os três lados são iguais

if lado1 == lado2 and lado2 == lado3:
    print("O triângulo é equilátero.")
else:
    print("O triângulo não é equilátero.")