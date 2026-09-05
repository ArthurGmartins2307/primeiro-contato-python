valor_conta = float(input('Qual foi o valor total da compra? '))
taxa_de_servico = valor_conta * 0.10
valor_total = valor_conta + taxa_de_servico
quantidade_pessoas = int(input('Quantas pessoas vão dividir? '))
juncao = (quantidade_pessoas, valor_total)
print(f'Quantidade total de pessoa: {juncao[0]} - Valor para cada pessoa: {juncao[1] / juncao[0]}')

