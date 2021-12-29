print('Gerando termos para a Progressão Aritmética!')
print('-=-' *20)
primeiro = int(input('Digite o primeiro valor: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont +=1
print('FIM')

