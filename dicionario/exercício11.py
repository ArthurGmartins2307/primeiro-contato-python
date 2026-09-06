despesas_amigos = {
    "João": [25.50, 40.00, 15.75],
    "Maria": [32.00, 18.50, 50.00],
    "Pedro": [10.00, 25.00, 30.50],
    "Ana": [45.00, 20.00, 12.50],
    "Carlos": [15.00, 35.50, 22.00]
}

for item in despesas_amigos:
  soma = 0
  for i in despesas_amigos[item]:
    soma += i
  print(f'{item} está devendo R${soma}')