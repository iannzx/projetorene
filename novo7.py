login = ''
senha = ''
logado = False
tent = 0
while login != 'angelin' or senha != 'abc123':
    login = input('Digite o login da rádio: ')
    senha = input('Digite sua senha: ')
    logado = True

    if logado:
        print ('menu')
        print('1- cadrastar radiolista: ')

    else:
        print('Voce perdeu acesso!')


