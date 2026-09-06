
palavras3 = {
    "maçã": "apple",
    "janela": "window",
    "nuvem": "cloud",
    "rio": "river",
    "teclado": "keyboard",
    "montanha": "mountain",
    "café": "coffee",
    "jardim": "garden",
    "computador": "computer",
    "amarelo": "yellow",
    "oceano": "ocean",
    "lápis": "pencil",
    "espelho": "mirror",
    "trovão": "thunder",
    "livro": "book",
    "liberdade": "freedom",
    "planeta": "planet",
    "sombra": "shadow",
    "música": "music",
    "floresta": "forest"
}
for i in palavras3:
  print(i)
palavra_user = input('Escreva uma dessas palavras que está na lista acima: ')

if palavra_user in palavras3:
    print(palavras3[palavra_user])
else:
    print("Essa palavra não está na lista.")
