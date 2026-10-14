# um cidadao decidiu criar um quarto inteligente no qual o quarto possui sensores e atuadores. 
# O objetivo é criar um algoritmo que facilite a noite de sono do morador, conferindo coforto termico e economia de energia.
# O algoritmo deve tbm controlar e proteger o quarto de assalto, chuva e entrada de animais indesejados(gatos de rua). 

hora = int(input("Digite a hora: "))

luminosidade = input("Está claro? (sim/nao): ")
temperatura = float(input("Digite a temperatura: "))
umidade = float(input("Digite a umidade: "))
presenca_quarto = input("Tem alguém no quarto? (sim/nao): ")
presenca_externa = input("Tem presença do lado de fora? (sim/nao): ")
chuva = input("Está chovendo? (sim/nao): ")

# Controle da janela
if chuva == "sim":
    print("Fechar janela por causa da chuva.")

elif presenca_externa == "sim":
    print("Fechar janela para proteger o quarto.")

elif hora >= 22 or hora < 6:
    print("Fechar janela durante a noite.")

elif luminosidade == "sim" and 6 <= hora < 18:
    print("Abrir janela para aproveitar a luz natural.")

else:
    print("Manter janela fechada.")


# Controle do ar-condicionado
if temperatura >= 28:
    print("Ligar ar-condicionado.")

elif temperatura <= 22:
    print("Desligar ar-condicionado.")

else:
    print("Manter ar-condicionado como está.")

    # Controle do ventilador
if temperatura >= 25 and temperatura < 28:
    print("Ligar ventilador.")

elif temperatura < 25:
    print("Desligar ventilador.")

else:
    print("Manter ventilador como está.")


# Controle do umidificador
if umidade < 40:
    print("Ligar umidificador.")

elif umidade >= 40:
    print("Desligar umidificador.")


# Proteção contra animais
if presenca_externa == "sim":
    print("Alerta! Presença detectada na área externa.")

elif presenca_externa == "nao":
    print("Área externa segura.")