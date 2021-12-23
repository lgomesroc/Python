#Quando a pessoa deve se alistar e verificar se é homem ou mulher
from datetime import date
atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
sexo = str(input('Digite seu sexo [M/F]: ')).upper()
if sexo == 'M':
    print(f'Quem nasceu em {nascimento} tem {idade} anos.')
    print(f'Você é do sexo masculino e tem que se alistar ou já se alistou.')
    if idade > 18:
        print(f'Já passou o tempo de alistamento. Há {idade-18} que passou os anos,')
        ano = atual - (idade - 18)
        print(f'O ano de alistamenfo foi em {ano}.')
    elif idade == 18:
        print(f'Está na hora de se alistar.')
    elif idade < 18:
        print(f'Ainda não chegou o tempo de alistamento. Falta {18-idade} anos.')
        ano = atual +(18-idade)
        print(f'O alistamento será em {ano}.')
elif sexo == 'F':
    print{f'Sexo digitado [e {sexo}. Você é mulher e por isso não é obrigada a se alistar.'}
else:
    print(f'Sexo inválido.')
