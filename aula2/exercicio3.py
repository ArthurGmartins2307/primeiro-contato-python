print("Escolha o tipo de conversão:")
print("1 - Celsius (°C) para Fahrenheit (°F)")
print("2 - Fahrenheit (°F) para Celsius (°C)")

opcao = input("Digite a opção (1 ou 2): ")

if opcao == "1":
    celsius = float(input("Digite a temperatura em °C: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius:.1f}°C correspondem a {fahrenheit:.1f}°F")
elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em °F: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit:.1f}°F correspondem a {celsius:.1f}°C")
else:
    print("Opção inválida.")