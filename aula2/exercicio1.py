print("Digite o primeiro numero:")
valor1 = float(input())
print("Digite o segundo numero:")
valor2 = float(input())
print("Escolha a operação: + - * /")
operacao = input()

if operacao == "+":
  print(f"Resultado:", valor1 + valor2)
elif operacao == "-":
  print(f"Resultado:", valor1 - valor2)
elif operacao == "*":
  print(f"Resultado:", valor1 * valor2)
elif operacao == "/":
  if valor2 == 0:
    print("Não é possível dividir por zero")
  else:
    print(f"Resultado:", valor1 / valor2)