meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]
print('Vendedores que bateram a meta:')
for i in vendas:
  nome, vendas = i
  if vendas >= meta:
    print(f'{nome}, com {vendas} vendas')