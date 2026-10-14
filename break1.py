opçao = 99

while opçao != 0:
    print('----------MENU----------')
    print('[1] para cadastrar pacientes ')
    print('[2] para buscar pacientes ')
    print('[3] para remover pacientes ')
    print('[0] para sair ')
    opçao = int(input('Digite a opçãp: '))
    if opçao == 0:
        break