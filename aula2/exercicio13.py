ingredientes = ['farinha', 'açúcar', 'ovos', 'leite', 'manteiga']

ingrediente_antigo = 'leite'
ingrediente_novo = 'água'

for i in range(len(ingredientes)):
    if ingredientes[i] == ingrediente_antigo:
        ingredientes[i] = ingrediente_novo

print(ingredientes)