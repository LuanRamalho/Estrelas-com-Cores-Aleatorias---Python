import tkinter as tk
import random
import math

# Função para gerar uma cor aleatória em hexadecimal
def cor_aleatoria():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Função para desenhar uma estrela
def desenhar_estrela(canvas, x, y, tamanho, cor):
    pontos = []
    for i in range(10):
        angulo = i * (360 / 10)  # Divide os 360 graus em 10 pontos para a estrela
        raio = tamanho if i % 2 == 0 else tamanho / 2
        x_ponto = x + raio * math.cos(math.radians(angulo))
        y_ponto = y + raio * math.sin(math.radians(angulo))
        pontos.append((x_ponto, y_ponto))
    canvas.create_polygon(pontos, fill=cor, outline='black')

# Função principal para criar estrelas em posições e tamanhos aleatórios
def desenhar_estrelas(canvas, quantidade):
    largura = int(canvas['width'])
    altura = int(canvas['height'])
    for _ in range(quantidade):
        x = random.randint(0, largura)
        y = random.randint(0, altura)
        tamanho = random.randint(20, 100)
        cor = cor_aleatoria()
        desenhar_estrela(canvas, x, y, tamanho, cor)

# Configuração da janela principal e do canvas
root = tk.Tk()
root.title("Estrelas Aleatórias")

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Desenhar 20 estrelas
desenhar_estrelas(canvas, 20)

root.mainloop()
