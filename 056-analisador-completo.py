somaidade = mediaidade = maioridadehomem = 0
nomehomem = ''
totmulher20 = 0
for p in range(1,5):
    print(f'---------------{p}ª PESSOA---------------')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Ssexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehomem = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomem = nome
    if sexo in 'Ff'and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f'A média da idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomehomem}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos,')