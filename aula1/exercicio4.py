print("Quanto metros quadrados tem a parede que você quer pintar?")
parede = float(input())
latasTinta = 0
precoLatas = latasTinta * 50
quantidadeTinta = 5 * latasTinta
metrosPintados = 3 * quantidadeTinta

while metrosPintados < parede:
    latasTinta += 1
    quantidadeTinta = 5 * latasTinta
    metrosPintados = 3 * quantidadeTinta
print(f"Você precisará de: {latasTinta} latas de tinta")


