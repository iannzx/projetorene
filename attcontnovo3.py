notas = []

for i in range(4):
    nota = float(input(f'Digite a {i + 1}ª nota: '))
    notas.append(nota)

media = sum(notas) / 4

print("Notas:", notas)
print("Média:", media)
