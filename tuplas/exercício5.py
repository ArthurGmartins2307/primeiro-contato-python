def media_e_quantidade():
  frase = input('Escreva uma frase: ')
  palavras = frase.split()
  qnt_palavras = len(palavras)
  soma_letras = 0
  for i in palavras:
    soma_letras += len(i)
  media = soma_letras / qnt_palavras

  juncao = (qnt_palavras, media)
  quantidade, media = juncao
  return(print(juncao))

media_e_quantidade()