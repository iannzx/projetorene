
voto = input('Qual seu voto? ')
if voto == '01' or voto == '02' or voto == '03' or voto == '04':
    print('seu voto foi valido')
elif voto == '00':
    print('seu voto foi em branco')
else:
    print('seu voto foi invalidado ou nulo')