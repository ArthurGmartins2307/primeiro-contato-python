
estoque = {
    "Notebook": 10,
    "Mouse": 25,
    "Teclado": 15,
    "Monitor": 8,
    "Headset": 20,
    "Webcam": 12,
    "Impressora": 5,
    "Pendrive": 30,
    "Cabo HDMI": 18,
    "Caixa de Som": 7
}

def adicionar_produto(nome, quantidade):
  estoque[nome] = quantidade

def remover_produto(nome):
  del estoque[nome]

adicionar_produto('fone', 8)
print(estoque)
remover_produto('Teclado')
print(estoque)