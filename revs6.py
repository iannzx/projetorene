#Questão 27

morangos = float(input('Digite a quantidade de morangos: '))
maças = float(input('Digite a quantidade de maças: '))

if morangos <= 5:
    v_morangos = morangos * 2.50
else: 
    v_morangos = morangos * 2.20

if maças <= 5:
    v_maças = maças * 1.80
else:
    v_maças = maças * 1.50

total = v_morangos + v_maças

if morangos + maças > 8 or total > 25:
    desconto = total * 0.10
    total = total - desconto

print('Valor a pagar: R$', total)