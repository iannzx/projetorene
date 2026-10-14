usuarios = [['Vitor', '345', False], ['Ian', '567', True]]

for usuario in usuarios:
    if usuario[2] == False:
      print('Usuario: ' + usuario[0])
    elif usuario[2] == True:
        print('Usuario ADM: ' + usuario[0])


print('1- LOGIN \n2- CADASTRAR USUARIO \n0- SAIR')
op = int(input('-> '))

if op == 1:
    user_nome = input('Digite seu nome: ')
    user_senha = input('Digite sua senha: ')

    for usuario in usuarios:
        usuario_achado = False
        if usuario[0] == user_nome and usuario[1] == user_senha: 
            usuario_achado = True

            break
        if usuario_achado:
            print('Login efetuado com sucesso')
        else:
            print('Senha ou usuario invalidos(a)')

if op == 2:
    cad_nome = input('Digite seu nome: ')
    cad_senha = input('Digite sua senha: ')
    cad_cpf = input('Digite seu CPF: ')
    cad_tele = input('Digite seu número de telefone: ')
    print('Usuario cadastrado com SUCESSO!')
    