print("Qual é a bebida?")
bebida = input()
print("Qual é o preço dessa bebida?")
preco = float(input())
print("Qual será a quantidade vendida dessa bebida?")
quantidade = int(input())
preco_final = preco * quantidade
print(f"O valor total da compra de {bebida} será de: R${preco_final}")
