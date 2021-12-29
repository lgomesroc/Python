resposta = 'S'
media = soma = quant = menor = maior = 0
while resposta in 'Ss':
    num = int(input('Digie um número: '))
    soma += num
    quant += 1
    if maior < num:
        maior = num
    else:
        menor = num
    resposta = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
media = soma / quant
print(f'A quantidade de valores é {quant} e a média é {media:.2f}')
print(f'O maior valor entre os digitados é {maior} e o menor valor é {menor}.')
