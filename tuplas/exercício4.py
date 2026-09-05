nome = input('Escreva o nome do produto: ')
preco = float(input('Escreva o preço do produto: '))
quantidade = int(input('Escreva a quantidade do produto: '))
produtos = (nome, preco)
nome, preco = produtos
print(f'valor total do estoque: R${preco * quantidade}')