print("Responda as perguntas com sim ou nao.")

qtd = 0

resposta1 = input("Telefonou para a vítima? ")
if resposta1 == "sim":
    qtd = qtd + 1

resposta2 = input("Esteve no local do crime? ")
if resposta2 == "sim":
    qtd = qtd + 1

resposta3 = input("Mora perto da vítima? ")
if resposta3 == "sim":
    qtd = qtd + 1

resposta4 = input("Devia para a vítima? ")
if resposta4 == "sim":
    qtd = qtd + 1

resposta5 = input("Já trabalhou com a vítima? ")
if resposta5 == "sim":
    qtd = qtd + 1

if qtd == 2:
    print('Suspeito')
if qtd == 3 or qtd == 4:
    print('Cumplice')
if qtd == 5:
    print('Assassino')
if qtd < 2:
    print('Não tem nada haver com isso. livre de tudo')