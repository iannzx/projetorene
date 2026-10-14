alc = float(input('Digite o valor do litro do alcool: '))
gaso = float(input('Digite o valor do litro da gasolina: '))

if alc <= gaso * 0.70:
    print('Compensa abastecer com alcool. ')
else:
    print('Compensa abastecer com gasolina. ')