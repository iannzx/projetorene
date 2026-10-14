#Operadores logicos
alt  = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
idd  = float(input('Qual sua idade? '))
quer = input('Quer dançar comigo?')

if alt > 1.60 and peso > 40 and idd >= 18 and quer == 'sim':
    print('Bora simbora')
else:
    print('Vou ali que meu amigo segundo tá chamando')