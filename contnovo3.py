#Tipos de dados
#string, float, integer, boolean

#tipos de estruturas de dados
#lista

lista_amg = ['ian', 'italo', 'thamires', 'carlos']
#percorrer a lista

busca = input('Digite o nome que procura: ')

for amigo in lista_amg:
    if busca in amigo:
        print('Seu amigo tá na lista: ', amigo)