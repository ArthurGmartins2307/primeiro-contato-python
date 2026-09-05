temperaturas = [
    (22, 25, 27, 24, 23),
    (18, 20, 21, 19, 22),
    (30, 32, 31, 29, 33),
    (15, 17, 16, 18, 14),
    (25, 27, 26, 28, 24),
    (20, 22, 23, 21, 19),
    (28, 30, 29, 31, 27)
]
fila = 0
soma = 0
semana = 1
mais_de_trita = 0
for i in range(len(temperaturas)):
  while fila < len(temperaturas[i]):
    if temperaturas[i][fila] > 30:
      mais_de_trita += 1
    soma += temperaturas[i][fila]
    fila += 1
  media = soma / len(temperaturas[i])
  print(f'Média da {semana}º semana: {media}')
  soma = 0
  semana += 1
  fila = 0
print(f'Vezes que a temperatura excedeu 30°C: {mais_de_trita}')