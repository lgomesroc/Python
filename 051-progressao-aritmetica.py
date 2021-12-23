#Programa para calcular a progressão aritmética onde o usuário escolhe o primeiro termo, quantos termos serão
# mostrados e a razão.
primeiro = int(input('Digite o primeiro número inteiro: '))
razao = int(input('Qual a razão: '))
termo = int(input(('Quantos termos quer amostra?: ')))
num = primeiro + (termo - 1) * razao
for c in range(primeiro,num + 1,razao):
    print(f'{c}', end=' -> ')
print(f'FINALIZADO!!!')
