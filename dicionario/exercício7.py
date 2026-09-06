frase = input('Escreva uma frase: ')
palavras = frase.split()
letras = []

for item in palavras:
  letras_palavra = 0
  for i in item:
    letras_palavra += 1
  letras.append(letras_palavra)

juntar = zip(palavras, letras)
dicionario = dict(juntar)
print(dicionario)
