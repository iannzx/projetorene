#QUESTAO 14 DA LISTA DE DECISÃO

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9.0 and media <=10:
    print("conceito A")
elif media >= 7.5:
    print("conceito B")
elif media >= 6.0:
    print("conceito C")
elif media >= 4.0:
    print("conceito D")
else:
    print("conceito E")