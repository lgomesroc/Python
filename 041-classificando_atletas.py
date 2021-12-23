#Categoria do atleta durante a sua idade
from datetime import date
anoatual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = anoatual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print(f'Classiicação MIRIM.')
elif idade <= 14:
    print(f'Classiicação INFANTIL.')
elif idade <= 19:
    print(f'Classificação JUNIOR.')
elif idade <= 25:
    print(f'Classificação SÊNIOR.')
else:
    print(f'Classificação MASTER.')
