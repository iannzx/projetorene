import random

palavras = [
    "python",
    "computador",
    "programacao",
    "internet",
    "teclado",
    "celular",
    "banana",
    "elefante",
    "futebol",
    "chocolate"
]

palavra = random.choice(palavras)
letras_descobertas = ["_"] * len(palavra)
letras_tentadas = []
erros = 0
max_erros = 6

print("================================")
print("        JOGO DA FORCA")
print("================================")

while erros < max_erros and "_" in letras_descobertas:

    print("\nPalavra:", " ".join(letras_descobertas))
    print("Letras tentadas:", ", ".join(letras_tentadas))
    print(f"Erros: {erros}/{max_erros}")

    # Conta quantas letras diferentes foram acertadas
    letras_corretas = len(set(letras_tentadas) & set(palavra))

    print(f"Letras corretas: {letras_corretas}/4")

    # Libera a tentativa da palavra inteira após 4 letras corretas
    if letras_corretas >= 4:
        print("\n🔓 Você acertou 4 letras!")
        print("Agora você pode tentar descobrir a palavra inteira.")

    tentativa = input("Sua tentativa: ").lower().strip()

    # Tentativa da palavra inteira
    if len(tentativa) > 1:

        if letras_corretas >= 4:

            if tentativa == palavra:
                print("\n🎉 PARABÉNS! Você descobriu a palavra!")
                print("A palavra era:", palavra)
                break

            else:
                print("❌ Palavra incorreta!")
                erros += 1
                continue

        else:
            print("❌ Você precisa acertar 4 letras primeiro!")
            continue

    # Verifica se foi digitada uma letra
    if len(tentativa) != 1 or not tentativa.isalpha():
        print("⚠️ Digite apenas uma letra!")
        continue

    letra = tentativa

    if letra in letras_tentadas:
        print("⚠️ Você já tentou essa letra!")
        continue

    letras_tentadas.append(letra)

    if letra in palavra:
        print("✅ Acertou!")

        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra

    else:
        erros += 1
        print("❌ Errou!")

else:

    if "_" not in letras_descobertas:
        print("\n🎉 PARABÉNS! Você ganhou!")
        print("A palavra era:", palavra)

    else:
        print("\n💀 Você perdeu!")
        print("A palavra era:", palavra)

print("\nFim de jogo!")
