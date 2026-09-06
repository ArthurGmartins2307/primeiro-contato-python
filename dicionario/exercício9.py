
alunos = {
    "João": [8.5, 7.0, 9.0],
    "Maria": [10.0, 8.5, 9.5],
    "Pedro": [6.0, 7.5, 8.0],
    "Ana": [9.0, 9.5, 10.0],
    "Carlos": [7.0, 6.5, 8.5]
}

def adicionar_nota(nome, nota):
  alunos[nome].append(nota)

def visualizar_media(nome):
  soma = 0
  for i in alunos[nome]:
    soma += i
  media = soma / len(alunos[nome])
  print(f'Média do(a) aluno(a): {media}')

visualizar_media('Ana')