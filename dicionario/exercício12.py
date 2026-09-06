quiz = {
    "Qual é a capital do Brasil? ": "Brasília",
    "Quanto é 5 + 5? ": "10",
    "Qual é o maior planeta do Sistema Solar? ": "Júpiter",
    "Quantos dias tem uma semana? ": "7",
    "Qual é a linguagem de programação que estamos estudando? ": "Python",
    "Qual é o resultado de 10 * 2? ": "20",
    "Qual é o maior oceano do mundo? ": "Pacífico",
    "Quantas letras tem a palavra Python? ": "6",
    "Qual é a capital da França? ": "Paris",
    "Quanto é 100 / 4 ?": "25"
}

for i in quiz:
  resposta = input(i )
  if resposta == quiz[i]:
    print('Resposta correta!')
  else:
    print('Resposta incorreta!')
  break