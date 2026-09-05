meta = 10000
vendas = [
    ['João', 1000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
#seu código aqui
for item in vendas:
    if item[1] >= meta:
        print('Vendedor {} bateu a meta. Fez {} vendas'.format(item[0], item[1]))