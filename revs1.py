idd = int(input('Digite sua idade: '))

if idd < 18 or idd > 34:
    print('você está fora dos parâmetros de normalidade para entrar na PF. ')
else:
    print('Você está dentro dos parâmetros de normalidade para entrar na PF.')