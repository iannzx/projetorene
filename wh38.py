inicial = 1995
sal_ini = float(input('Quanto você ganha? '))
aum = 1.5 / 100 #1996
#1997 em diante dobra o percentual

for ano in range(1996,2026):
    sal_ini = sal_ini * (1 + aum)
    print(f'no ano de {ano} ele ganha {sal_ini:.2f}')
    aum = aum * 2
