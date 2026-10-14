login = ''
senha = ''
logado = False
tent = 0
while tent < 5 and logado == False:
    login = input('Digite o login da rádio: ')
    senha = input('Digite sua senha: ')
    if login == 'angelin' or senha == 'abc123':
        logado = True
    else:
        tent += 1
        print(' quantidade de tentativas restantes: ',5- tent)
    

if logado:
    print ('MENU')
    print('1- cadastrar radialista')
else:
    print('Voce errou o acesso')