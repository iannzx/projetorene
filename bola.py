import tkinter as tk
import math

# Criar janela
janela = tk.Tk()
janela.title("Bola girando")

largura = 400
altura = 350

canvas = tk.Canvas(janela, width=largura, height=altura, bg="black")
canvas.pack()

# Centro e tamanho da órbita
cx = largura // 2
cy = altura // 2
raio = 100

angulo = 0

def animar():
    global angulo

    # Calcular posição da bolinha
    x = cx + math.cos(angulo) * raio
    y = cy + math.sin(angulo) * raio

    # Criar uma cor RGB que muda com o tempo
    r = int((math.sin(angulo) + 1) * 127)
    g = int((math.sin(angulo + 2) + 1) * 127)
    b = int((math.sin(angulo + 4) + 1) * 127)

    cor = f"#{r:02x}{g:02x}{b:02x}"

    # Apagar tudo
    canvas.delete("all")

    # Desenhar órbita
    canvas.create_oval(
        cx - raio, cy - raio,
        cx + raio, cy + raio,
        outline="gray"
    )

    # Desenhar bolinha
    tamanho = 20
    canvas.create_oval(
        x - tamanho, y - tamanho,
        x + tamanho, y + tamanho,
        fill=cor,
        outline=""
    )

    # Aumentar o ângulo
    angulo += 0.05

    # Repetir a animação
    janela.after(16, animar)

animar()
janela.mainloop()
