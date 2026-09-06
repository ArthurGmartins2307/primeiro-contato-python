
def contagem(palavras):
  palavras.split()
  contagem = {}

  for item in palavras:
    for i in item:
      if i != ' ':
        if i in contagem:
          contagem[i] += 1
        else:
          contagem[i] = 1
  print(contagem)

contagem('palavras que se repetem')
