#Mostrando quantas pessoas são menores e maiores com tratamento de dados inválidos como anos
# negativos e maiores que 120.
from datetime import date
atual = date.today().year
totmaior = totmenor = 0
for pessoa in range(1,8):
    nasc = int(input(f'Digite o ano de nascimento da {pessoa}ª pessoa: '))
    idade = atual - nasc
    if 18 > idade >= 0:
        print(f'{idade}.')
        totmenor += 1
        print(f'É MENOR!')
    elif 18 < idade < 120:
        print(f'{idade}.')
        totmaior +=1
        print(f'É MAIOR!')
    elif idade < 0 or idade >= 120:
        print('Não existe idade maior que 120 ou menor que zero(0). Idade inválida')
        break
print(f'O total de {totmenor} de menores e {totmaior} de maiores')

