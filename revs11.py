nome = input("Digite seu nome: ")

a = input("Algoritmos: ")
c = input("Cálculo 1: ")
o = input("AOC: ")
i = input("Inglês: ")
p = input("Português: ")

if a == "ruim":
    a = 1
elif a == "bom":
    a = 2
else:
    a = 3
if c == "ruim":
    c = 1
elif c == "bom":
    c = 2
else:
    c = 3
if o == "ruim":
    o = 1
elif o == "bom":
    o = 2
else:
    o = 3
if i == "ruim":
    i = 1
elif i == "bom":
    i = 2
else:
    i = 3
if p == "ruim":
    p = 1
elif p == "bom":
    p = 2
else:
    p = 3
print("Aluno:", nome)
print("Média:", (a + c + o + i + p) / 5)