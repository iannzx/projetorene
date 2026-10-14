area = float(input("Digite a área do imóvel em m²: "))
sanitaria = input("A finalidade é sanitária? (sim/não): ")

if area > 200:
    vistoria = input("Deseja a vistoria especial gratuita? (sim/não): ")

    if vistoria == "sim":
        print("Vistoria especial gratuita.")
    else:
        valor = area * 500
        print("Valor da licença: R$", valor)

elif sanitaria == "sim":
    valor = area * 120
    print("Valor da licença: R$", valor)

else:
    valor = area * 70
    print('Valor da licença: R$', valor)  