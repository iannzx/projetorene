#Questão 5


repetir = "s"

while repetir == "s":
    a = int(input("População A: "))
    taxa_a = float(input("Taxa A (%): "))

    b = int(input("População B: "))
    taxa_b = float(input("Taxa B (%): "))

    while a <= 0 or b <= 0 or taxa_a <= 0 or taxa_b <= 0:
        print("Valores inválidos!")
        
        a = int(input("População A: "))
        taxa_a = float(input("Taxa A (%): "))
        b = int(input("População B: "))
        taxa_b = float(input("Taxa B (%): "))

    anos = 0

    while a < b:
        a = a + a * taxa_a / 100
        b = b + b * taxa_b / 100
        anos += 1

    print("Anos necessários:", anos)

    repetir = input("Deseja repetir? (s/n): ")

print("Programa encerrado.")
