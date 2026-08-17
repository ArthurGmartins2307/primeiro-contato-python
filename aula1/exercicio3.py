precoFabrica = 170000
percentualDistro = 28
imposto = 45
calculoDistro = (percentualDistro / 100) * precoFabrica
calculoImposto = (imposto / 100) * precoFabrica
print("Preco do percentual da distribuição:", calculoDistro)
print("Preço dos impostos sobre o carro:", calculoImposto)
print("O preço do carro fica em:", calculoImposto + calculoDistro + precoFabrica)