def contar_letras(palavra):
    vogal = 0
    consoante = 0

    for i in palavra:
        if i in 'aeiou':
            vogal += 1
        elif i.isalpha():
            consoante += 1

    return (vogal, consoante)


palavra = input('Escreva uma palavra: ')

resultado = contar_letras(palavra)

print(f'Vogais: {resultado[0]} - Consoantes: {resultado[1]}')