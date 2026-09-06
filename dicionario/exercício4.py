chaves = ['nome', 'idade', 'nota']
alunos = []

def criar_aluno():
  nome = input('Qual é o nome do aluno? ')
  idade = int(input('Qual é a idade do aluno? '))
  nota = float(input('Qual foi a nota do aluno? '))
  aluno = [nome, idade, nota]
  juntar2= zip(chaves, aluno)
  dicionario2 = dict(juntar2)
  alunos.append(dicionario2)

def mostrar_aluno(int):
  print(alunos[int])

criar_aluno()
mostrar_aluno(0)
