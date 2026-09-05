import math
valor_aluguel = float(input('Qual é o valor do aluguel? '))
despesas = float(input('Qual foi o valor das despesas? '))
pessoas = int(input('Quantas pessoas foram? '))
valor_total = valor_aluguel + despesas
dividir = math.ceil(valor_total / pessoas)
print(f'Valor que cada um deverá que pagar: {dividir}')