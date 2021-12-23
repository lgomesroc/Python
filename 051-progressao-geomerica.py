#Programa para calcular a progressão geomética onde o usuário escolhe o primeiro termo, quantos termos serão
# mostrados e a razão porém mostra o mesmo valor e quero que mostre uma sequencia de números.
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = int(input('Quantos termos?: '))
num = primeiro * razao**(termo-1)
for c in range(1, termo +1):
    print(f'{num} ', end='-> ')
print(f'FINALIZADO!!!')


