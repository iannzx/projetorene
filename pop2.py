op = -1
banda = []
while op != 0:
    print('------ FESTIVAL ROCK PB ------')
    print('1 - Cadastrar bandas')
    print('2 - Remover bandas')
    print('3- Listar bandas')
    print('0- SAIR')
    op = int(input('Digite a opção desejada: '))

    if op == 1:
        nome = input('Digite o nome da banda: ')
        banda.append(nome)
    elif op == 2:
        busca = input('Digite o nome da banda para remover')
        ind = -1
    for i in range(len(banda)):
        if busca == banda[i]:
            ind = i
    if ind == -1:
        print('Banda não encontrada')
    else:
        banda.pop(ind) #pop remove pelo indice
        print('Banda removida com sucesso')