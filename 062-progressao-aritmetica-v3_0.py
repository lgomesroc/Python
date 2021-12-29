print('Gerando termos para a Progressão Aritmética')
print('-=' * 20)
primeiro = int(input('Digite o primeiro valor: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end=' ')
        print('-> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você deseja mostrar a mais? '))
print(f'Progressão aritmética finalizada com {total} termos mostrados.')
