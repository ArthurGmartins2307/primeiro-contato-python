jogadores = []

quantidade = int(input('Quantos jogadores? '))

for i in range(quantidade):
    nome = input('Nome do jogador: ')
    pontuacao = int(input('Pontuação: '))

    jogadores.append((nome, pontuacao))

jogadores.sort(key=lambda jogador: jogador[1], reverse=True)

print('\nRanking:')

for i in range(len(jogadores)):
    print(f'{i + 1}º - {jogadores[i][0]}: {jogadores[i][1]} pontos')

