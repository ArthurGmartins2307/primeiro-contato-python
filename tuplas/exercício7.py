def ocorrencias(lista, valor):
    quantidade = 0

    for elemento in lista:
        if elemento == valor:
            quantidade += 1

    total = len(lista)

    return (quantidade, total)


numeros = [1, 2, 3, 2, 4, 2, 5]

resultado = ocorrencias(numeros, 2)

print(resultado)